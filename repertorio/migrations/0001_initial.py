# Generated by Django 5.1.7 on 2025-03-28 08:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('artista', models.CharField(max_length=200)),
                ('repertorio', models.CharField(choices=[('actual', 'Repertorio Actual'), ('villancicos', 'Villancicos'), ('otros', 'Otros Repertorios'), ('inedito', 'Inédito'), ('olvidadas', 'Canciones Olvidadas')], max_length=20)),
                ('partitura', models.FileField(blank=True, null=True, upload_to='partituras/')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
