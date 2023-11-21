from django import forms
from django.utils.safestring import mark_safe

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Your Email'})
        )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Your Password'})
        )

