from django import forms
from .models import Pizza, Cliente

class OrderPizzaForm(forms.Form):

    OPTIONS = (
        (1, "Pizza Personal"),
        (2, "Pizza Mediana"),
        (3, "Pizza Grande"),
    )

    pizzas = forms.ChoiceField(widget=forms.RadioSelect,choices=OPTIONS)

class OrderIngredienteForm(forms.Form):

    OPTIONS = (
        (1, "Jamon"),
        (2, "Champiñones"),
        (3, "Pimenton"),
        (4, "Doble Queso"),
        (5, "Pepperoni"),
        (6, "Aceitunas"),
        (7, "Salchichon"),
    )

    ingredientes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido']

