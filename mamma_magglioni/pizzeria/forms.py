from django import forms
from .models import Pizza, Cliente

class OrderForm(forms.Form):

    OPTIONS = (
        (1, "Pizza Personal"),
        (2, "Pizza Mediana"),
        (3, "Pizza Grande"),
    )

    pizza = forms.ChoiceField(widget=forms.RadioSelect,choices=OPTIONS)

    OPTIONS2 = (
        (1, "Jamon"),
        (2, "Champiñones"),
        (3, "Pimenton"),
        (4, "Doble Queso"),
        (5, "Pepperoni"),
        (6, "Aceitunas"),
        (7, "Salchichon"),
    )

    ingredientes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS2, required=False)

class ClienteForm(forms.Form):
    OPTIONS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    nombre = forms.CharField(label='Nombre', widget= forms.TextInput(attrs= { 'class': 'form-control'}))
    apellido = forms.CharField(label='Apellido', widget= forms.TextInput(attrs= { 'class': 'form-control'}))
    pizzas = forms.IntegerField(widget=forms.Select(choices=OPTIONS, attrs= { 'class': 'form-control'}))

"""class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido']"""

