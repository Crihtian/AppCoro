from django import forms
from .models import Cancion

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = [
            'nombre', 'artista', 'repertorio', 'partitura',
            'soprano_midi', 'mezzosoprano_midi', 
            'contralto_midi', 'contralto2_midi',
            'tenor_midi', 'tenor2_midi',
            'baritono_midi', 'bajo_midi'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.TextInput(attrs={'class': 'form-control'}),
            'repertorio': forms.Select(attrs={'class': 'form-control'}),
            'partitura': forms.FileInput(attrs={'class': 'form-control'}),
            'soprano_midi': forms.FileInput(attrs={'class': 'form-control'}),
            'mezzosoprano_midi': forms.FileInput(attrs={'class': 'form-control'}),
            'contralto_midi': forms.FileInput(attrs={'class': 'form-control'}),
            'contralto2_midi': forms.FileInput(attrs={'class': 'form-control'}),
            'tenor_midi': forms.FileInput(attrs={'class': 'form-control'}),
            'tenor2_midi': forms.FileInput(attrs={'class': 'form-control'}),
            'baritono_midi': forms.FileInput(attrs={'class': 'form-control'}),
            'bajo_midi': forms.FileInput(attrs={'class': 'form-control'}),
        } 