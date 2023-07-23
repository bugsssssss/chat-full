from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser): 
    first_name = models.CharField(("First name"), max_length=100)
    username = models.CharField(("username"), max_length=50, blank=True, unique=True, null=True)
    email = models.EmailField(("email"), max_length=254, blank=True)
    age = models.IntegerField(("age"), blank=True, null=True)
    about = models.TextField(("about"), blank=True)
    password = models.CharField(("password"), max_length=100)
    created = models.DateTimeField(("created"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.first_name


class Message(models.Model):

    sender = models.ForeignKey("main.User", verbose_name=("sender"), on_delete=models.CASCADE)
    text = models.TextField(("text"))
    created = models.DateTimeField(("created"), auto_now=False, auto_now_add=True)



    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    # def __str__(self):
    #     return self.id



class Chat(models.Model):
    messages = models.ManyToManyField("main.Message", verbose_name=("messages"))
    created = models.DateTimeField(("created"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Chat")
        verbose_name_plural = ("Chats")

    # def __str__(self):
    #     return self.id

