from django import forms
from django.utils.safestring import mark_safe

class PassData(forms.Form):
    # pass_data = forms.CharField(
    #     max_length = 200,
    #     label='pass_data'
    #     )
    pass_data = forms.IntegerField(
        label='pass_data'
        )