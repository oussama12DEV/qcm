from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from .models import Utilisateur
class Creetulisateur(UserCreationForm):
     class Meta:
        model=User
        fields=['username','email','password1','password2']