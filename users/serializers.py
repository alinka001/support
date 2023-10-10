from .models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_employee', 'password')
        # extra_kwargs = {'password': {'write_only': True}}
        #
        # def create(self, validated_data):
        #     username = validated_data.get('username')
        #     email = validated_data.get('email')
        #     first_name = validated_data.get('first_name')
        #     last_name = validated_data.get('last_name')
        #     password = validated_data.get('password')
        #     is_employee = validated_data.get('is_employee')
        #
        #     try:
        #         user = User.objects.create_user(username=username,
        #                                         email=email,
        #                                         first_name=first_name,
        #                                         last_name=last_name,
        #                                         is_employee=is_employee,
        #                                         password=password,
        #                                         )
        #     except ValidationError as e:
        #         raise serializers.ValidationError({'username': e})
        #     return user


# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         # username = serializers.CharField()
#         # password = serializers.CharField()
#         def validate(self, data):
#
#             username = data.get('username')  # compare with?
#             password = data.get('password')
#
#             if username and password:
#                 return data
#             else:
#                 raise serializers.ValidationError('username and password is not valid')



