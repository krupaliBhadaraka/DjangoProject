from django import forms
from django.contrib.auth.models import User
from LoginApp.models import LoginModel


class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = LoginModel
        fields = '__all__'
