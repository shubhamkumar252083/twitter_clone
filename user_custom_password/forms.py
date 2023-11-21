
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add any additional customization in the __init__ method

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get('new_password1')
        # Add your custom validation logic here
        return new_password1
