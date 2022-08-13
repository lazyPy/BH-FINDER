from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password1', 'password2']
