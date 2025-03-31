from django import forms
from .models import Cancion

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['nombre', 'artista', 'repertorio', 'partitura']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.TextInput(attrs={'class': 'form-control'}),
            'repertorio': forms.Select(attrs={'class': 'form-control'}),
            'partitura': forms.FileInput(attrs={'class': 'form-control'}),
        } 