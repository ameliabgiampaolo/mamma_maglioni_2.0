from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.db.models.expressions import RawSQL
from django.db import connection
from .forms import OrderForm, ClienteForm
from .models import Pedido, Pizza_ing, Cliente, Pizza, Ingrediente
from django.forms import formset_factory
import datetime

def index(request):
    context = {} 
    return render(request, 'pizzeria/index.html', context)

def cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.create_cliente(form.cleaned_data.get('nombre'), form.cleaned_data.get('apellido'))
            return redirect('order', cliente.id, form.cleaned_data.get('pizzas'))
    else:
        form = ClienteForm()

    return render(request, 'pizzeria/cliente.html', { 'form': form })

def calcular_precio(pizza_ing):
    precio_pizzas = 0
    precio_ingredientes = 0
    num_pizza = 1
    for i in range(len(pizza_ing)):
        if pizza_ing[i].num_pizza == num_pizza:
            precio_pizzas += pizza_ing[i].fk_pizza.precio
            num_pizza += 1

        if pizza_ing[i].fk_ingrediente != None:
            precio_ingredientes += pizza_ing[i].fk_ingrediente.precio
    
    return precio_pizzas + precio_ingredientes

def order(request, cliente_id, pizzas):
    date = datetime.date.today()
    OrderFormset = formset_factory(OrderForm,extra=pizzas)
    aux = 1 #variable para controlar cada pizza
    pizzas = []

    if request.method == 'POST':
        formset = OrderFormset(request.POST)
        if formset.is_valid():
            pedido = Pedido.objects.create_pedido(date, Cliente.objects.get(id=cliente_id))
            for form in formset:
                pizza = form.cleaned_data.get('pizza')
                ingredientes = form.cleaned_data.get('ingredientes') 
                if ingredientes != []:
                    for i in range(len(ingredientes)):
                        pizza_ing = Pizza_ing.objects.create_pizza_ing(Pizza.objects.get(id=pizza), Ingrediente.objects.get(id=ingredientes[i]), pedido, aux)
                        pizzas.append(pizza_ing)
                else:
                    pizza_ing = Pizza_ing.objects.create_pizza_ing(Pizza.objects.get(id=pizza), None, pedido, aux)
                    pizzas.append(pizza_ing)

                aux += 1
            
            precio_total = calcular_precio(pizzas)
            pedido.precio_total = precio_total
            pedido.save()

            return redirect('resumen', pedido.id)
    else:
        formset = OrderFormset()

    return render(request, 'pizzeria/order_form.html', { 'formset': formset })

def resumen(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    date = pedido.fecha.strftime("%d-%m-%Y")
    cliente = Cliente.objects.get(id=pedido.fk_cliente_id)
    pizza_ing = Pizza_ing.objects.filter(fk_pedido_id=pedido_id) #filter lo uso para traer varios registros de la bd, varias pizza_ing con ese pedido
    context = {'cliente': cliente, 'pedido': pedido, 'pizza_ing': pizza_ing, 'date': date}
    return render(request, 'pizzeria/resumen.html', context)

def finalizar(request):
    return render(request, 'pizzeria/finalizar.html')

def delivery(request, fk_cliente_id):
    cliente = Cliente.objects.get(id=fk_cliente_id)
    context = {'cliente': cliente}
    return render(request, 'pizzeria/delivery.html', context)

def finalizar_delivery(request):
    return render(request, 'pizzeria/finalizar_delivery.html')

def reporte(request):
    return render(request,'pizzeria/reportes.html')

def reporte1(request):
    ventas = Pedido.objects.all().order_by('id')
    context = {'ventas': ventas}
    return render(request,'pizzeria/reporte1.html', context)

def reporte2(request):
    fechas = Pedido.objects.order_by('fecha').values('fecha').distinct()
    pedidos = Pedido.objects.all()
    test = Pizza_ing.objects.all()
    for pedido in test:
        print(pedido)
    context = {'fechas': fechas,'pedidos': pedidos}
    return render(request,'pizzeria/reporte2.html',context)

def reporte3(request):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT p.size,
                        (SELECT COUNT(i.fk_pizza_id) FROM pizzeria_pizza_ing i WHERE i.fk_pizza_id = p.id)"Unidades vendidas",
                        (SELECT COUNT(f.fk_pizza_id)*p.precio FROM pizzeria_pizza_ing f WHERE f.fk_pizza_id = p.id)"Total generado"
                        FROM pizzeria_pizza p;""")
        ventas_pizza = cursor.fetchall()
    context = {'pizzas': ventas_pizza}
    return render(request,'pizzeria/reporte3.html',context)

def reporte4(request):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT i.nombre,
                          (SELECT COUNT(v.fk_ingrediente_id) FROM pizzeria_pizza_ing v WHERE v.fk_ingrediente_id = i.id)"Unidades Vendidas",
                          (SELECT COUNT(v.fk_ingrediente_id)*i.precio FROM pizzeria_pizza_ing v WHERE v.fk_ingrediente_id = i.id)"Total generado"
                          FROM pizzeria_ingrediente i;""")
        ventas_ingredientes = cursor.fetchall()
    context = {'ingredientes': ventas_ingredientes}
    return render(request,'pizzeria/reporte4.html',context)

def reporte5(request):
    nombres = Cliente.objects.values('nombre','apellido').distinct()
    pedidos = Pedido.objects.all()
    for nombre in nombres:
        print(nombre)
    for pedido in pedidos:
        print(pedido)
    context = {'nombres': nombres,'pedidos': pedidos}
    return render(request,'pizzeria/reporte5.html', context)