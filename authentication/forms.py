from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
