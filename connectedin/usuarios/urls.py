from django.urls import path
from .views import *

from django.contrib.auth import views

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', login, name='login'),
]
