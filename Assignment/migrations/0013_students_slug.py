# Generated by Django 4.1.2 on 2022-10-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0012_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
