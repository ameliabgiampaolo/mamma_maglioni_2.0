from django.db import models

class ClienteManager(models.Manager):
    def create_cliente(self, nombre, apellido):
        cliente = self.create(nombre=nombre, apellido=apellido)
        cliente.save()
        return cliente

class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)
    objects = ClienteManager()

    def __str__(self):
        return '#' + str(self.id) + ' | ' + self.nombre + ' | ' + self.apellido

    def id(self):
        return self.id

class PedidoManager(models.Manager):
    def create_pedido(self, fecha, fk_cliente):
        pedido = self.create(fecha=fecha, fk_cliente=fk_cliente)
        pedido.save()
        return pedido

class Pedido(models.Model):
    fecha = models.DateField('fecha del pedido')
   # precio_total = models.DecimalField(max_digits=8, decimal_places=2)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    objects = PedidoManager()

    def __str__(self):
        return '#' + str(self.id) + ' | ' + self.fecha + ' | fk_cliente = ' + str(self.fk_cliente)

    def id(self):
        return self.id
 
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

class Pizza_ingManager(models.Manager):
    def create_pizza_ing(self, fk_pizza, fk_ingrediente, fk_pedido):
        pizza_ing = self.create(fk_pizza=fk_pizza, fk_ingrediente=fk_ingrediente, fk_pedido=fk_pedido)
        pizza_ing.save()
        return pizza_ing

class Pizza_ing(models.Model):
    fk_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    fk_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    fk_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    objects = Pizza_ingManager()

    def __str__(self):
        return '#' + str(self.id) + ' | fk_pizza = ' + str(self.fk_pizza) + ' | fk_ingrediente = ' + str(self.fk_ingrediente) + ' | fk_pedido = ' + str(self.fk_pedido)