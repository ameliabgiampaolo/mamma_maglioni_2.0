from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import OrderForm, ClientForm
from .models import Pedido, Pizza_ing, Cliente, Pizza, Ingrediente
from django.forms import formset_factory
import datetime

def index(request):
    context = {} 
    return render(request, 'pizzeria/index.html', context)

def cliente(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.create_cliente(form.cleaned_data.get('nombre'), form.cleaned_data.get('apellido'))
            return redirect('order', cliente.id, form.cleaned_data.get('cantidad'))
    else:
        form = ClientForm()

    return render(request, 'pizzeria/cliente.html', { 'form': form })

def order(request, cliente_id, cantidad):
    now = datetime.date.today()
    x = cantidad
    OrderFormset = formset_factory(OrderForm,extra=x)
    if request.method == 'POST':
        formset = OrderFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data.get('pizzas')) 
                print(form.cleaned_data.get('ingredientes')) 
            
            return redirect('resumen', 3)
    else:
        formset = OrderFormset()

    return render(request, 'pizzeria/order_form.html', { 'formset': formset })

"""def order(request):
    ingrediente = False
    now = datetime.date.today()
    if request.method == 'POST':
        form_pizza = OrderPizzaForm(request.POST)
        form_ingrediente = OrderIngredienteForm(request.POST)
        form_client = ClientForm(request.POST)

        if form_pizza.is_valid():
            pizzas = form_pizza.cleaned_data.get('pizzas')
        
        if form_ingrediente.is_valid():
            ingredientes = form_ingrediente.cleaned_data.get('ingredientes')
            ingrediente = True

        if form_client.is_valid():
            cliente = form_client.save() 


        pedido = Pedido.objects.create_pedido(now, cliente)

        if ingrediente == True:
            for i in range(len(ingredientes)):
                pizza_ing = Pizza_ing.objects.create_pizza_ing(Pizza.objects.get(id=pizzas), Ingrediente.objects.get(id=ingredientes[i]), pedido)
        else:
            pizza_ing = Pizza_ing.objects.create_pizza_ing(Pizza.objects.get(id=pizzas),None,pedido)

        return redirect('resumen', pedido.id)
    else:
        form_pizza = OrderPizzaForm
        form_ingrediente = OrderIngredienteForm
        form_client = ClientForm

    return render(request, 'pizzeria/order_form.html', { 'form':form_pizza, 'form2':form_ingrediente, 'form3': form_client })"""

def resumen(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    cliente = pedido.fk_cliente_id
    context = {'cliente': cliente}
    return render(request, 'pizzeria/resumen.html', context)