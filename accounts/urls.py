from django.urls import path
from accounts.views import SignInView, SignUpView, UserView

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('me/', UserView.as_view(), name='me'),
]