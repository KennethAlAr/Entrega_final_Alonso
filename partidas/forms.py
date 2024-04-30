from django import forms
from django.contrib.auth.models import User
from .models import Avatar

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email"
        ]

class JuegoSearchForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Ingresar nombre del juego")

class SistemaSearchForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Ingresar nombre del sistema")

class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["image"]