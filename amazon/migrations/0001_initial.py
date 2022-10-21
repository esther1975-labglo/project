# Generated by Django 4.1.2 on 2022-10-20 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('Stock_availability', models.CharField(max_length=50)),
            ],
        ),
    ]
