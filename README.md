# Sistema de Gestión de Repertorio Coral

Este proyecto es un sistema web para gestionar repertorios corales, diseñado específicamente para directores de coro y músicos. Permite organizar y acceder a partituras y archivos MIDI de diferentes voces de manera eficiente.

## Características Principales

- 🎵 Gestión de repertorios corales
- 📄 Almacenamiento de partituras en PDF
- 🎹 Archivos MIDI separados por voz
- 👥 Sistema de roles (Directores)
- 🔒 Autenticación de usuarios
- 📱 Interfaz responsiva

## Requisitos

- Python 3.8+
- Django 4.2+
- PostgreSQL
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Crihtian/AppCoro
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. Realizar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

```
repertorio/
├── manage.py
├── requirements.txt
├── repertorio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── decorators.py
│   └── urls.py
└── templates/
    ├── base.html
    ├── lista_canciones.html
    └── agregar_cancion.html
```

## Uso

1. Acceder al sistema con credenciales de director
2. Ver lista de canciones organizadas por repertorio
3. Agregar nuevas canciones con sus respectivos archivos
4. Gestionar partituras y archivos MIDI

## Contribuir

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Tu Nombre - [@tutwitter](https://twitter.com/tutwitter) - email@ejemplo.com

Link del Proyecto: [https://github.com/tu-usuario/repertorio-coral](https://github.com/tu-usuario/repertorio-coral) 
