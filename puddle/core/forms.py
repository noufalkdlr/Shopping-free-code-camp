from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs= {' class': 'form-control', 'placeholder': 'enter password' })
    )

    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

    username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs= {' class': 'form-control', 'placeholder': 'Enter email' })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs= {' class': 'form-control', 'placeholder': 'enter password' })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs= {' class': 'form-control', 'placeholder': 'repeat password' })
    )
