# Generated by Django 4.1.1 on 2022-09-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0002_marksheet_students_delete_mark_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='marksheet',
            name='science',
            field=models.IntegerField(default=90),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='social',
            field=models.IntegerField(default=80),
        ),
    ]
