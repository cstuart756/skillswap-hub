from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Email or Username",
        widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "username"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "current-password"}),
    )
