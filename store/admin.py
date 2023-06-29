from django.contrib import admin

from .models import *

admin.site.register(Cliente)
admin.site.register(Product)
admin.site.register(Orden)
admin.site.register(OrdenItem)
admin.site.register(DireccionPedido)
