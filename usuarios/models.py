from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    CUERDA_CHOICES = [
        ('soprano', 'Soprano'),
        ('mezzosoprano', 'Mezzosoprano'),
        ('contralto', 'Contralto'),
        ('tenor', 'Tenor'),
        ('baritono', 'Barítono'),
        ('bajo', 'Bajo'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cuerda = models.CharField(max_length=20, choices=CUERDA_CHOICES)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_cuerda_display()}"
