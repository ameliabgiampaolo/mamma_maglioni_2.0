from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderPizzaForm, OrderIngredienteForm

def index(request):
    context = {} 
    return render(request, 'pizzeria/index.html', context)

def order(request):
    if request.method == 'POST':
        form_pizza = OrderPizzaForm(request.POST)
        form_ingrediente = OrderIngredienteForm(request.POST)
        if form_pizza.is_valid():
            pizzas = form.cleaned_data.get('pizzas')
        if form_ingrediente.is_valid():
            ingredientes = form.cleaned_data.get('ingredientes')
        # do something with your results
    else:
        form = OrderPizzaForm
        form2 = OrderIngredienteForm

    return render(request, 'pizzeria/order_form.html', {'form':form, 'form2':form2 })
    
    
    
    """form = OrderForm()
    return render(request, 'pizzeria/order_form.html',{'form':form})
    pass"""
