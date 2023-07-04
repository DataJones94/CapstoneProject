from django.shortcuts import render
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import CoachSerializer
from .models import Coach
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_coaches(request):
    
    coaches = Coach.objects.all()
    serializer = CoachSerializer(coaches, many=True)
    return Response(serializer.data)
    


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def client_detail(request, user_id):  
    print(
    'User', f"{request.user.id}{request.user.email}{request.user.username}")    
    if request.method == 'POST':
        serializer = CoachSerializer(data=request.data)
        if serializer.is_valid():                                     
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        coach = CoachSerializer.objects.filter(user_id=user_id)
        serializer = CoachSerializer(coach, many=True)
        return Response(serializer.data) 

# Create your views here.
