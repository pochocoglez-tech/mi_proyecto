from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistroUsuarioForm(UserCreationForm):

    username = forms.CharField(
        label='Usuario',
        help_text='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingresa tu usuario'
        })
    )

    password1 = forms.CharField(
        label='Contraseña',
        help_text='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ingresa tu contraseña'
        })
    )

    password2 = forms.CharField(
        label='Confirmar contraseña',
        help_text='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirma tu contraseña'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']