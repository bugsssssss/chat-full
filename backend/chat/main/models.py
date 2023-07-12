from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser): 
    first_name = models.CharField(("First name"), max_length=100)
    email = models.EmailField(("email"), max_length=254, blank=True)
    age = models.IntegerField(("age"), blank=True, null=True)
    about = models.TextField(("about"), blank=True)
    password = models.CharField(("password"), max_length=50)
    created = models.DateTimeField(("created"), auto_now=False, auto_now_add=True)

