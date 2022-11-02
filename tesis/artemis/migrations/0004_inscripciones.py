# Generated by Django 4.1.1 on 2022-11-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artemis', '0003_remove_diplomados_cursos_req_diplomados_cursos_req'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('capacidad', models.IntegerField()),
                ('diplomado', models.ManyToManyField(to='artemis.diplomados')),
                ('estudiantes', models.ManyToManyField(to='artemis.estudiantes')),
            ],
        ),
    ]
