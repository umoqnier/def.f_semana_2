from django.contrib import admin
from .models import Remainder  # La clase de nuestros models

class RemainderAdmin(admin.ModelAdmin):  # Admin model admin lo hereda
    pass

admin.site.register(Remainder, RemainderAdmin)  # Se le pasa el modelo a renderear y la clase de administrador
