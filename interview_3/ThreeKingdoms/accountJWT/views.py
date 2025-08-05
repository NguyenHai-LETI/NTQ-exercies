from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



def login_html(request):
    return render(request, 'accountJWT/login_page.html')

class RegisterView(APIView):
    permission_classes = [AllowAny] # cho phép mọi người truy cập
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Thông tin đăng nhập không hợp lệ'}, status=status.HTTP_401_UNAUTHORIZED)


# Protected view - cần xác thực để truy cập
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated] # chỉ cho ng đã xác thực truy cập

    def get(self, request):
        content = {'message': f'Hi, {request.user.username}! Successfully logged in!'}
        return Response(content, status=status.HTTP_200_OK)
