from django.contrib import admin
from .models import Cliente, Pedido, Ingrediente, Pizza, Pizza_ing

class Pizza_ingAdmin(admin.ModelAdmin):
    list_display  =  ( 'fk_pedido', 'fk_ingrediente', 'fk_pizza', 'num_pizza',  )
    list_filter = ['fk_pedido__fecha','fk_pizza__size', 'fk_ingrediente__nombre', 'fk_pedido__fk_cliente__nombre']
    search_fields = ['=fk_pedido__id', 'fk_pedido__fk_cliente__nombre', 'fk_pedido__fk_cliente__apellido', '=fk_ingrediente__nombre', '=fk_pizza__size','fk_pedido__fecha']
    list_per_page = 20
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Ventas'}
        return super(Pizza_ingAdmin, self).changelist_view(request, extra_context=extra_context)

class PizzaAdmin(admin.ModelAdmin):
    list_display  =  ( 'id','size', 'precio', )
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Pizzas'}
        return super(PizzaAdmin, self).changelist_view(request, extra_context=extra_context)

class IngreAdmin(admin.ModelAdmin):
    list_display  =  ( 'id','nombre', 'precio', )
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Ingredientes'}
        return super(IngreAdmin, self).changelist_view(request, extra_context=extra_context)

class ClienteAdmin(admin.ModelAdmin):
    list_display  =  ( 'id','nombre', 'apellido',  )
    list_filter = ['nombre', 'apellido' ]
    search_fields = ['nombre', 'apellido',]
    list_per_page = 20
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Clientes'}
        return super(ClienteAdmin, self).changelist_view(request, extra_context=extra_context)

class PedidoAdmin(admin.ModelAdmin):
    list_display  =  ( 'id','fecha', 'fk_cliente' )
    list_filter = ['fecha', 'fk_cliente__nombre', 'fk_cliente__apellido' ]
    search_fields = ['fecha', 'fk_cliente__nombre', 'fk_cliente__apellido']
    list_per_page = 20
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Pedidos'}
        return super(PedidoAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Ingrediente, IngreAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pizza_ing , Pizza_ingAdmin)