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
            return redirect('order', cliente.id, form.cleaned_data.get('cantidad'))
    else:
        form = ClienteForm()

    return render(request, 'pizzeria/cliente.html', { 'form': form })

def order(request, cliente_id, cantidad):
    date = datetime.date.today()
    OrderFormset = formset_factory(OrderForm,extra=cantidad)
    aux = 1 #variable para controlar cada pizza

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
                else:
                    pizza_ing = Pizza_ing.objects.create_pizza_ing(Pizza.objects.get(id=pizza), None, pedido, aux)

                aux += aux
            
            return redirect('resumen', pedido.id)
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
    cliente = Cliente.objects.get(id=pedido.fk_cliente_id)
    pizza_ing = Pizza_ing.objects.filter(fk_pedido_id=pedido_id) #filter lo uso para traer varios registros de la bd, varias pizza_ing con ese pedido
    context = {'cliente': cliente, 'pedido': pedido, 'pizza_ing': pizza_ing}
    return render(request, 'pizzeria/resumen.html', context)

def finalizar(request):
    return render(request, 'pizzeria/finalizar.html')