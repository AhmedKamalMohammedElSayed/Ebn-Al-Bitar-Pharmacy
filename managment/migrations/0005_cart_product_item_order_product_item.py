# Generated by Django 4.2.2 on 2023-06-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0004_remove_cart_prduct_item_remove_order_prduct_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_item',
            field=models.ManyToManyField(null=True, to='managment.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='product_item',
            field=models.ManyToManyField(null=True, to='managment.product'),
        ),
    ]