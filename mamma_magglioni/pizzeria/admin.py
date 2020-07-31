from django.contrib import admin
from .models import Cliente, Pedido, Ingrediente, Pizza, Pizza_ing

class Pizza_ingAdmin(admin.ModelAdmin):
    list_display  =  ( 'fk_pedido', 'fk_ingrediente', 'fk_pizza', 'num_pizza',  )
    list_filter = ['fk_pizza', 'fk_ingrediente','fk_pedido' ]
    search_fields = ['=fk_pedido__id', 'fk_pedido__fk_cliente__nombre', 'fk_pedido__fk_cliente__apellido', '=fk_ingrediente__nombre', '=fk_pizza__size']
    list_per_page = 10

class PizzaAdmin(admin.ModelAdmin):
    list_display  =  ( 'id','size', 'precio', )
    list_per_page = 10

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Ingrediente)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pizza_ing , Pizza_ingAdmin)