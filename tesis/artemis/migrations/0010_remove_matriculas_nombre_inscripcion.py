# Generated by Django 4.1.1 on 2023-03-13 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artemis', '0009_remove_matriculas_capacidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matriculas',
            name='nombre_inscripcion',
        ),
    ]
