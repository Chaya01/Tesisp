# Generated by Django 4.1.1 on 2023-02-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artemis', '0006_cuotas_matriculas_periodo_delete_inscripciones_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriculas',
            name='precio',
            field=models.IntegerField(default=10000000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuotas',
            name='fecha_emision',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cuotas',
            name='fecha_exp',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuotas',
            name='fecha_pago',
            field=models.DateField(blank=True, null=True),
        ),
    ]
