# Generated by Django 3.0.8 on 2020-07-20 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=12)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='fecha del pedido')),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzeria.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=9)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza_ing',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fk_ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzeria.Ingrediente')),
                ('fk_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzeria.Pedido')),
                ('fk_pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzeria.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='adicionales',
            field=models.ManyToManyField(through='pizzeria.Pizza_ing', to='pizzeria.Ingrediente'),
        ),
    ]