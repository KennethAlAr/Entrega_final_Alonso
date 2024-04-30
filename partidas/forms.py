from django import forms
from django.contrib.auth.models import User
from .models import Avatar, Sistema, Dado, Base

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
    nombre = forms.CharField(max_length=50, required=False, label="Buscar juego")
    disponible = forms.BooleanField(required=False, label="Mostrar solo juegos disponibles")
    jugadores_minimos = forms.IntegerField(required=False, label="Jugadores mínimos")
    sistema = forms.ModelChoiceField(queryset=Sistema.objects.all(), required=False, label="Filtrar por sistema de juego")
    fecha = forms.DateField(required=False, label="Buscar por fecha", widget=forms.DateInput(attrs={'type': 'date'}))

class SistemaSearchForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=False, label="Ingresar nombre del sistema")
    tipo_dado = [('', '---------')] + list(Dado.choices)
    tipo_base = [('', '---------')] + list(Base.choices)
    dado = forms.ChoiceField(choices=tipo_dado, required=False, label="Tipo de dado")
    base = forms.ChoiceField(choices=tipo_base, required=False, label="Base del sistema")

class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["image"]