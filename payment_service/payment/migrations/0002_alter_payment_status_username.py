# Generated by Django 4.1.6 on 2023-03-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_status',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
