from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto', 'calificacion']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'calificacion': forms.Select(attrs={'class': 'form-control'}),
        }