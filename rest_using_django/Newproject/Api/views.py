from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import userserializer

# Create your views here.

@api_view(['Get'])
def get_users(request):
    users = User.objects.all()
    serializer =userserializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer=userserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get', 'PUT','DELETE' ])
def user_detail(request,pk):
    try:
        user=User.object.get(pk=pk)
    except User.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Serialzer = userserializer(user)
        return Response(Serialzer.data)
    
    
    if request.method == 'PUT':
        serializer=userserializer(user, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
