from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Comentario

class RegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = (
            'username',
            'email',
            'telefono',
            'municipio',
            'password1',
            'password2',
        )

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
