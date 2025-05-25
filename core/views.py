from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status



# Create your views here.

class LoginAPIView(APIView):
    def post(self,request):
        # taking username and password from user
        username = request.data.get('username')
        password = request.data.get('password')
        if username == None and password == None:
            raise ValidationError({
                "details":"Both username and password required."
            })
            #It checks if the username and password match a user in the database.
        user = authenticate(username = username,password = password)
        if user:
            # 1)It checks if a token already exists for that user,2)If YES,it gets the token and if NO it creates a new token.
            token,_=Token.objects.get_or_create(user=user)
            # If user found then It sends back the token and username
            return Response({
                "token":token.key,
                "username":user.username
            },status=status.HTTP_202_ACCEPTED)
            # If user not found then It sends back an error message
        return Response({
            "details":"User is not registered"
        },status=status.HTTP_401_UNAUTHORIZED)
        
    