from django.urls import path
from .views import *
urlpatterns = [
    path('auth/', Authentication.as_view(), name='auth'),
    path('register/', register, name='register')
]
