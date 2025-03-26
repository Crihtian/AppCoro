from django.contrib import admin
from .models import Cancion

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'artista', 'repertorio')
    list_filter = ('repertorio',)
    search_fields = ('nombre', 'artista')
    ordering = ('repertorio', 'nombre')
