from django.contrib import admin
from inventarioslist_app.models import Ciudad, Comercial, Empresa, Ot, Producto, Actualizacion

# Register your models here.
admin.site.register(Comercial)
admin.site.register(Empresa)
admin.site.register(Producto)
admin.site.register(Actualizacion)
admin.site.register(Ot)
admin.site.register(Ciudad)