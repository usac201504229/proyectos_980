# Generated by Django 3.0 on 2020-11-12 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='foto',
        ),
    ]
