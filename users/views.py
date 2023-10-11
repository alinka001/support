from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

from .serializers import UserSerializer  # , LoginSerializer
from .models import User
from rest_framework import generics, permissions, status
from django.contrib.auth import authenticate, login
from rest_framework.response import Response


# class RegistrationView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]
#
#
# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
#     #permission_classes = [permissions.AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         print(request.data)
#         serializer.is_valid(raise_exception=True)
#
#         username = serializer.validated_data.get('username')
#         password = serializer.validated_data('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return Response({'message': 'login successful'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'login not successful'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    print(user)
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)