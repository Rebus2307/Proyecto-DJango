# recomendaciones/admin.py
from django.contrib import admin
from .models import Usuario, Libro, Recomendacion

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Recomendacion)
