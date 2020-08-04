from django.db import models

class ClienteManager(models.Manager):
    def create_cliente(self, nombre, apellido):
        cliente = self.create(nombre=nombre, apellido=apellido)
        cliente.save()
        return cliente

class Cliente(models.Model):
    nombre = models.CharField(max_length=15, verbose_name="Nombre Cliente")
    apellido = models.CharField(max_length=20, verbose_name="Apellido Cliente")
    objects = ClienteManager()

    def __str__(self):
        return '#' + str(self.id) + ' | ' + self.nombre + ' | ' + self.apellido

class PedidoManager(models.Manager):
    def create_pedido(self, fecha, fk_cliente):
        pedido = self.create(fecha=fecha, fk_cliente=fk_cliente)
        pedido.save()
        return pedido

class Pedido(models.Model):
    fecha = models.DateField('fecha del pedido')
    precio_total = models.FloatField(default=0,null=True)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    objects = PedidoManager()
    def __str__(self):
        return '#' + str(self.id) + ' | ' + str(self.fecha) +' | ' + str(self.precio_total) + ' | fk_cliente = ' + str(self.fk_cliente)
 
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=12, verbose_name="Ingrediente")
    precio = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return '#' + str(self.id) + ' | ' + str(self.nombre) + ' | ' + str(self.precio)

class Pizza(models.Model):
    size  = models.CharField(max_length=9, verbose_name="Tamaño Pizza")
    precio = models.IntegerField()
    adicionales = models.ManyToManyField(
        Ingrediente,
        through='Pizza_ing'
    )

    def __str__(self):
        return '#' + str(self.id) + ' | ' + self.size + ' | ' + str(self.precio)

class Pizza_ingManager(models.Manager):
    def create_pizza_ing(self, fk_pizza, fk_ingrediente, fk_pedido, num_pizza):
        pizza_ing = self.create(fk_pizza=fk_pizza, fk_ingrediente=fk_ingrediente, fk_pedido=fk_pedido, num_pizza=num_pizza)
        pizza_ing.save()
        return pizza_ing

class Pizza_ing(models.Model):
    class Meta:
        verbose_name_plural = "Ventas"
    fk_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, verbose_name="Pizzas")
    fk_ingrediente = models.ForeignKey(Ingrediente, null=True, blank=True, on_delete=models.CASCADE,verbose_name="Ingredientes")
    fk_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name="Pedidos")
    num_pizza = models.IntegerField(default=1)
    objects = Pizza_ingManager()

    def __str__(self):
        return '#' + str(self.id) + ' | fk_pizza = ' + str(self.fk_pizza) + ' | fk_ingrediente = ' + str(self.fk_ingrediente) + ' | fk_pedido = ' + str(self.fk_pedido)