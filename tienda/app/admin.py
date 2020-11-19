from django.contrib import admin
from .models import Marca, Producto, Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca"]
    search_fields = ["nombre"]


admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)



