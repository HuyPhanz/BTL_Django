# Generated by Django 4.1.6 on 2023-03-21 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
    ]
