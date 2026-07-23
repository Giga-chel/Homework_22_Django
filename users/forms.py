from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country')