# Generated by Django 4.1.2 on 2022-10-25 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0009_alter_cart_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 10, 46, 9, 944648)),
        ),
    ]
