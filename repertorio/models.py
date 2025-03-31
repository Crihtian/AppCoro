from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Director(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario.username

class Cancion(models.Model):
    REERTORIO_CHOICES = [
        ('actual', 'Repertorio Actual'),
        ('villancicos', 'Villancicos'),
        ('otros', 'Otros Repertorios'),
        ('inedito', 'Inédito'),
        ('olvidadas', 'Canciones Olvidadas'),
    ]
    
    nombre = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    repertorio = models.CharField(max_length=20, choices=REERTORIO_CHOICES)
    partitura = models.FileField(upload_to='partituras/', null=True, blank=True)
   
    
    def __str__(self):
        return f"{self.nombre} - {self.artista}"
