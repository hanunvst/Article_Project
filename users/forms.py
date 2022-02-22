
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




