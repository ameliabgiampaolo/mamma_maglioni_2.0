from django import forms
from .models import Pizza

class OrderPizzaForm(forms.Form):

    OPTIONS = (
        ("PP", "Pizza Personal"),
        ("PM", "Pizza Mediana"),
        ("PG", "Pizza Grande"),
            )
    Pizzas = forms.ChoiceField(widget=forms.RadioSelect,choices=OPTIONS)

class OrderIngredienteForm(forms.Form):

    OPTIONS = (
        ("JA", "Jamon"),
        ("CH", "Champiñones"),
        ("PI", "Pimenton"),
        ("DQ", "Doble Queso"),
        ("PE", "Pepperoni"),
        ("AC", "Aceitunas"),
        ("SA", "Salchichon"),
            )
    Ingredientes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

    