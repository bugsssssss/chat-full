from django.shortcuts import render
from .models import * 
from .serializers import * 
from rest_framework import generics,views, status
from django.db.models import Q, Avg
from rest_framework.response import Response
from rest_framework.decorators import api_view



class Authentication(views.APIView):

    def get(self, request):
        email = request.GET.get('email')
        password = request.GET.get('password')

        if email and password:
            try:
                instance = User.objects.get(Q(email=email) & Q(password=password))
                return Response({'id': instance.id})
            except:
                return Response(False)
            
        



@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
