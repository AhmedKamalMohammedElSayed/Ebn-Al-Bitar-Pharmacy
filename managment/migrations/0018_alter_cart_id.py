# Generated by Django 4.2.2 on 2023-06-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0017_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, unique=True),
        ),
    ]