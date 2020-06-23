from django.contrib import admin
from .models import Veiculo, Modelo, Motor

# Register your models here.
admin.site.register(Veiculo)
admin.site.register(Modelo)
admin.site.register(Motor)
