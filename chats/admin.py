from django.contrib import admin

from .models import Chats, ChatMessage

admin.register(Chats)
admin.register(ChatMessage)