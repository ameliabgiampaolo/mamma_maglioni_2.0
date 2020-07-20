from django.contrib import admin

from .models import Cliente, Pedido, Ingrediente, Pizza, Pizza_ing

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Ingrediente)
admin.site.register(Pizza)
admin.site.register(Pizza_ing)