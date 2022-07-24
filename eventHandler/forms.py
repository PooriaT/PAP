from django import forms
from .models import Userprofile

class UserprofileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userprofile