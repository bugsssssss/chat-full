from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'email', 'age']



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'created']



@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
