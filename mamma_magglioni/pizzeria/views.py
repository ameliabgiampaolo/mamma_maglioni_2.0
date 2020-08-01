from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
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

def calcular_precio(pedido, pizza_ing):
    pass

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
