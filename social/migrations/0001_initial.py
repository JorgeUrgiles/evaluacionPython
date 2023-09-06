# Generated by Django 4.2.4 on 2023-09-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(unique=True, verbose_name='Nombre clave')),
                ('name', models.CharField(max_length=50, verbose_name='Red Social')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'ordering': ['name'],
            },
        ),
    ]
