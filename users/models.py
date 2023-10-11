from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=150)
    is_employee = models.BooleanField(default=False)
    id = models.AutoField(unique=True, primary_key=True, editable=False)

    USERNAME_FIELD = 'username'
