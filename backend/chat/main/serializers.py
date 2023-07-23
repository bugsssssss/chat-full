from .models import * 
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ['first_name', 'email', 'password']


class ChatSerializer(serializers.ModelSerializer):

    messages = serializers.SerializerMethodField()

    def get_messages(self, obj):
        arr = [{'sender': x.sender.first_name,'text':x.text, 'created': x.created} for x in obj.messages.all()]
        return arr

    class Meta:
        model = Chat
        fields = '__all__'