from django.contrib import admin
from .models import Cliente, Pedido, Ingrediente, Pizza, Pizza_ing

class Pizza_ingAdmin(admin.ModelAdmin):
    list_display  =  ( 'fk_pizza', 'fk_ingrediente', 'fk_pedido', 'num_pizza',  )
    list_filter = ['fk_pizza', 'fk_ingrediente','fk_pedido' ]
    search_fields = ['fk_pedido']
    list_per_page = 10

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Ingrediente)
admin.site.register(Pizza)
admin.site.register(Pizza_ing, Pizza_ingAdmin)