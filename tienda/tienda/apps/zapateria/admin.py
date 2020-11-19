from django.contrib import admin
from .models import Facturacion, Zapato, Tarjeta, Pedido
# Register your models here.

admin.site.register(Facturacion)
admin.site.register(Zapato)
admin.site.register(Tarjeta)
admin.site.register(Pedido)