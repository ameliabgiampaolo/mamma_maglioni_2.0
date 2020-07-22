from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)

    def __str__(self):
        return '#' + str(self.id) + ' | ' + self.nombre + ' | ' + self.apellido

class Pedido(models.Model):
    fecha = models.DateField('fecha del pedido')
    precio_total = models.DecimalField(max_digits=8, decimal_places=2)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return '#' + str(self.id) + ' | ' + self.fecha + ' | ' + str(self.precio_total) + ' | ' + self.fk_cliente
 
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=12)
    precio = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return '#' + str(self.id) + ' | ' + self.nombre + ' | ' + str(self.precio)

class Pizza(models.Model):
    size  = models.CharField(max_length=9)
    precio = models.IntegerField()
    adicionales = models.ManyToManyField(
        Ingrediente,
        through='Pizza_ing'
    )

    def __str__(self):
        return '#' + str(self.id) + ' | ' + self.size + ' | ' + str(self.precio)

class Pizza_ing(models.Model):
    fk_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    fk_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    fk_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return '#' + str(self.id) + ' | fk_pizza = ' + str(self.fk_pizza) + ' | fk_ingrediente = ' + str(self.fk_ingrediente) + ' | fk_pedido = ' + str(self.fk_pedido)