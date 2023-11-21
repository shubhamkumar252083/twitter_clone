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


class AddTweetForm(forms.Form):
    tweet = forms.CharField(
        max_length = 200,
        label='tweet'
        )

class SearchTweetForm(forms.Form):
    search_tweet = forms.CharField(
        max_length = 200,
        label='search_tweet'
        )

class EditTweetForm(forms.Form):
    edit_tweet = forms.CharField(
        max_length = 200,
        label='edit_tweet'
        )