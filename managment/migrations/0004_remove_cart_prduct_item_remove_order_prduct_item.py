# Generated by Django 4.2.2 on 2023-06-17 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0003_cart_prduct_item_order_prduct_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='prduct_item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='prduct_item',
        ),
    ]
