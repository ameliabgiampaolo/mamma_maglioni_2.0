from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente', views.cliente, name='cliente'),
    path('order/<int:cliente_id>/<int:cantidad>', views.order, name='order'),
    path('resumen/<int:pedido_id>', views.resumen, name='resumen'),
]