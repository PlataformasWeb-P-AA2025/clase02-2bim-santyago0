from django.contrib import admin

# Register your models here.
from app1.models import Estudiante, Ciudad

admin.site.register(Estudiante)
admin.site.register(Ciudad)