from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente', views.cliente, name='cliente'),
    path('order/<int:cliente_id>/<int:pizzas>', views.order, name='order'),
    path('resumen/<int:pedido_id>', views.resumen, name='resumen'),
    path('finalizar', views.finalizar, name='finalizar'),
    path('finalizar_delivery', views.finalizar_delivery, name='finalizar_delivery'),
    path('delivery/<int:fk_cliente_id>', views.delivery, name='delivery'),
    path('reporte', views.reporte, name='reporte')
]