from .models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_employee', 'password')
