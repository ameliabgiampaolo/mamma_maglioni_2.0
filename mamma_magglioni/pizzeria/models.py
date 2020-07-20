from django.db import models

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)

class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField('fecha del pedido')
    precio_total = models.DecimalField(max_digits=8, decimal_places=2)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Ingrediente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=12)
    precio = models.DecimalField(max_digits=4, decimal_places=2)

class Pizza(models.Model):
    id = models.IntegerField(primary_key=True)
    size  = models.CharField(max_length=9)
    precio = models.IntegerField()
    adicionales = models.ManyToManyField(
        Ingrediente,
        through='Pizza_ing'
    )

class Pizza_ing(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    fk_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    fk_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)