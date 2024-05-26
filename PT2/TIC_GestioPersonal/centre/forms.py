# centre/forms.py
from django import forms
from .models import Usuari, Rol

class UsuariForm(forms.ModelForm):
    class Meta:
        model = Usuari
        fields = ['nom', 'cognom', 'assignatures', 'rol']

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nom']
