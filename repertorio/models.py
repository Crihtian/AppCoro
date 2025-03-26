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
    
    VOZ_CHOICES = [
        ('soprano', 'Soprano'),
        ('mezzosoprano', 'Mezzosoprano'),
        ('contralto', 'Contralto'),
        ('contralto2', 'Contralto 2'),
        ('tenor', 'Tenor'),
        ('tenor2', 'Tenor 2'),
        ('baritono', 'Barítono'),
        ('bajo', 'Bajo'),
    ]
    
    nombre = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    repertorio = models.CharField(max_length=20, choices=REERTORIO_CHOICES)
    partitura = models.FileField(upload_to='partituras/', null=True, blank=True, help_text='Archivo PDF de la partitura')
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Campos para los MIDIs de cada voz
    soprano_midi = models.FileField(upload_to='midis/', null=True, blank=True, help_text='Archivo MIDI para soprano')
    mezzosoprano_midi = models.FileField(upload_to='midis/', null=True, blank=True, help_text='Archivo MIDI para mezzosoprano')
    contralto_midi = models.FileField(upload_to='midis/', null=True, blank=True, help_text='Archivo MIDI para contralto')
    contralto2_midi = models.FileField(upload_to='midis/', null=True, blank=True, help_text='Archivo MIDI para contralto 2')
    tenor_midi = models.FileField(upload_to='midis/', null=True, blank=True, help_text='Archivo MIDI para tenor')
    tenor2_midi = models.FileField(upload_to='midis/', null=True, blank=True, help_text='Archivo MIDI para tenor 2')
    baritono_midi = models.FileField(upload_to='midis/', null=True, blank=True, help_text='Archivo MIDI para barítono')
    bajo_midi = models.FileField(upload_to='midis/', null=True, blank=True, help_text='Archivo MIDI para bajo')
    
    def __str__(self):
        return f"{self.nombre} - {self.artista}"
    
    def get_voces_disponibles(self):
        """Retorna un diccionario con las voces que tienen MIDI disponible"""
        voces = {}
        for voz in self.VOZ_CHOICES:
            if getattr(self, f"{voz[0]}_midi"):
                voces[voz[0]] = voz[1]
        return voces
