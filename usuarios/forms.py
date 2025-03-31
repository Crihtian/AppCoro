from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioAdminForm(forms.ModelForm):
    CUERDA_CHOICES = [
        ('soprano', 'Soprano'),
        ('mezzosoprano', 'Mezzosoprano'),
        ('contralto', 'Contralto'),
        ('tenor', 'Tenor'),
        ('baritono', 'Barítono'),
        ('bajo', 'Bajo'),
    ]

    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    username = forms.CharField(max_length=30, required=True, label='Nombre de Usuario')
    cuerda = forms.ChoiceField(choices=CUERDA_CHOICES, required=True, label='Cuerda')
    
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'username', 'cuerda')
        
    def save(self, commit=True):
        # Crear el usuario con contraseña provisional fija
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password='CoroJovenGijon'
        )
        
        # Crear el perfil de usuario
        usuario = super().save(commit=False)
        usuario.user = user
        if commit:
            usuario.save()
        return usuario 