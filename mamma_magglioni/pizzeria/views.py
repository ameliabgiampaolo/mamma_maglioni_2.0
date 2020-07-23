from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrderPizzaForm, OrderIngredienteForm
from .models import Pedido, Pizza_ing, Cliente, Pizza, Ingrediente
import datetime

def index(request):
    context = {} 
    return render(request, 'pizzeria/index.html', context)

def order(request):
    now = datetime.date.today()
    if request.method == 'POST':
        form_pizza = OrderPizzaForm(request.POST)
        form_ingrediente = OrderIngredienteForm(request.POST)
        if form_pizza.is_valid():
            pizzas = form_pizza.cleaned_data.get('pizzas')
        if form_ingrediente.is_valid():
            ingredientes = form_ingrediente.cleaned_data.get('ingredientes')

        cliente = Cliente.objects.create_cliente('Victor', 'Garcia')
        pedido = Pedido.objects.create_pedido(now, cliente)

        for i in range(len(ingredientes)):
            pizza_ing = Pizza_ing.objects.create_pizza_ing(Pizza.objects.get(id=pizzas), Ingrediente.objects.get(id=ingredientes[i]), pedido)

        return redirect('/pizzeria/')
    else:
        form_pizza = OrderPizzaForm
        form_ingrediente = OrderIngredienteForm

    return render(request, 'pizzeria/order_form.html', { 'form':form_pizza, 'form2':form_ingrediente })