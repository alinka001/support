from django.urls import path, include
from .views import signup, login  # , LoginView

urlpatterns = [
    path('register/', signup, name='registration'),
    path('login/', login, name='login')
]
