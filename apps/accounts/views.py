from django.shortcuts import render
from .serializers import SignupSerializer, SigninSerilizer, LogoutSerializer,UserProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .task import send_login_email
# Create your views here.

class SignupView(APIView):
    def post(self,request):
        print("post-")
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"user created","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response({"msg":serializer.errors},status = status.HTTP_400_BAD_REQUEST)

        
class SigninView(APIView):
    def post(self, request):
        print("signin--")
        serializer = SigninSerilizer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request,email=email,password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                send_login_email.delay(user.email)
                return Response({"refresh":str(refresh),"access":str(refresh.access_token)},status=status.HTTP_200_OK)
        
            else:
                return Response(
                    {"msg":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
                )
        return Response({"msg":"Bad Request"},status=status.HTTP_400_BAD_REQUEST)

class SignoutView(APIView):
    permission_class = [IsAuthenticated]

    def post(self, request):
        serializer  = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Logged Out successfully"})

      
class UserProfile(APIView):
    permission_class=[IsAuthenticated]

    def get(self,request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    
    def patch(self,request):
        data = request.data
        serializer = UserProfileSerializer(request.user,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":f"Updated user data for{request.user}","data":serializer.data})