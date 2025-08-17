from django.db import models
from accounts.models import User

class Chats(models.Model):
    from_user = models.ForeignKey(User, related_name='chats_from_user_id', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='chats_to_user_id', on_delete=models.CASCADE)
    viewed = models.DateTimeField(null=True)
    deleted = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      db_table = 'chats'

class  ChatMessage(models.Model):
   body = models.TextField(null=True)
   attachment_code = models.TextField(
      choices = [('FILE', 'FILE'), ('AUDIO', 'AUDIO')],
      max_length=10,
      null=True
   )
   attachment_id = models.IntegerField(null=True)
   viewed_at = models.DateTimeField(null=True)
   deleted_at = models.DateTimeField(null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   chat = models.ForeignKey(Chats, on_delete=models.CASCADE)
   from_user = models.ForeignKey(User,  on_delete=models.CASCADE)
