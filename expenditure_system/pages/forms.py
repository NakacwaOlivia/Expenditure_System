# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import User model


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    checkbox_field = forms.BooleanField(required=False)

    class Meta:
        model = User
        # Add 'checkbox_field' if you have it
        fields = ['user_name', 'email', 'password',
                  'confirm_password', 'checkbox_field']
