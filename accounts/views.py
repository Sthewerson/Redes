from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed

from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils.timezone import now

from rest_framework_simplejwt.tokens import RefreshToken

from accounts.auth import Authentication
from accounts.serializers import UserSerializer
from accounts.models import User

from core.utils.exceptions import ValidationError

import uuid


class SignInView(APIView, Authentication):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        signin = self.signin(email, password)

        if not signin:
            raise AuthenticationFailed

        user = UserSerializer(signin).data
        access_token = RefreshToken.for_user(signin).access_token

        return Response({
            "user": user,
            "access_token": str(access_token)
        })


class SignUpView(APIView, Authentication):
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data.get('name', '')
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        if not name or not email or not password:
            raise AuthenticationFailed

        signup = self.signup(name, email, password)

        if not signup:
            raise AuthenticationFailed

        user = UserSerializer(signup).data
        access_token = RefreshToken.for_user(signup).access_token

        return Response({
            "user": user,
            "access_token": str(access_token)
        })


class UserView(APIView):
    def get(self, request):
        # Update last_access
        User.objects.filter(id=request.user.id).update(last_access=now())

        user = UserSerializer(request.user).data

        return Response({
            "user": user
        })

    def put(self, request):
    # Coleta os dados (podem vir ausentes)
        name = request.data.get('name', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        avatar_file = request.FILES.get('avatar', None)

        storage = FileSystemStorage(
            settings.MEDIA_ROOT / "avatars",
            settings.MEDIA_URL + "avatars"
        )

        old_avatar_url = request.user.avatar
        new_avatar_url = None

        # Upload opcional do avatar
        if avatar_file:
            content_type = avatar_file.content_type
            ext = avatar_file.name.split('.')[-1].lower()

            if content_type not in ("image/png", "image/jpeg"):
                raise ValidationError("Somente arquivos do tipo PNG ou JPEG são suportados")

            saved_name = storage.save(f"{uuid.uuid4()}.{ext}", avatar_file)
            new_avatar_url = storage.url(saved_name)

        # Monte apenas os campos que realmente vieram
        data = {}
        if name is not None:
            data["name"] = name
        if email is not None:
            data["email"] = email
        if new_avatar_url is not None:
            data["avatar"] = new_avatar_url

        serializer = UserSerializer(request.user, data=data, partial=True)

        if not serializer.is_valid():
            # rollback do upload se falhar
            if new_avatar_url:
                try:
                    storage.delete(new_avatar_url.split("/")[-1])
                except Exception:
                    pass
            first_error = list(serializer.errors.values())[0][0]
            raise ValidationError(first_error)

        # Salva campos básicos
        user = serializer.save()

        # Atualiza senha, se enviada
        if password:
            user.set_password(password)
            user.save()

        # Remove avatar antigo se trocou e não for o padrão
        if new_avatar_url and old_avatar_url != "/media/avatars/default-avatar.png":
            try:
                storage.delete(old_avatar_url.split("/")[-1])
            except Exception:
                pass

        return Response({"user": UserSerializer(user).data})
