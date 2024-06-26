# Generated by Django 4.1.1 on 2023-03-02 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artemis', '0007_matriculas_precio_alter_cuotas_fecha_emision_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matriculas',
            name='precio',
        ),
        migrations.AddField(
            model_name='diplomados',
            name='precio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='matriculas',
            name='estudiantes',
        ),
        migrations.AddField(
            model_name='matriculas',
            name='estudiantes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artemis.estudiantes'),
            preserve_default=False,
        ),
    ]
