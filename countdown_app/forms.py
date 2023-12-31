from django import forms
from .models import Timer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

# FIX 3 (XSS)
# class TimerForm(forms.ModelForm):
#     class Meta:
#         model = Timer
#         fields = ['title', 'expiration_date']
#         widgets = {
#             'expiration_date': forms.DateInput(attrs={'type': 'date'}),
#         }
