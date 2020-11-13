# Generated by Django 3.0 on 2020-11-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201112_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('correo', models.EmailField(max_length=254)),
                ('edad', models.IntegerField(max_length=2)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]