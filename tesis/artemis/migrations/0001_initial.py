# Generated by Django 4.1.1 on 2022-10-31 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Becas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_beca', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profesiones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_profesion', models.CharField(max_length=20)),
                ('area_profesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artemis.areas')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('rut_estudiante', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_estudiante', models.CharField(max_length=30)),
                ('apellido_estudiante', models.CharField(max_length=20)),
                ('num_tel_estudiante', models.IntegerField(max_length=10)),
                ('direccion_estudiante', models.CharField(max_length=30)),
                ('beca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artemis.becas')),
                ('profesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artemis.profesiones')),
            ],
        ),
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('rut_docente', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_docente', models.CharField(max_length=20)),
                ('apellido_docente', models.CharField(max_length=20)),
                ('num_tel_docente', models.IntegerField(max_length=20)),
                ('profesion_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artemis.profesiones')),
            ],
        ),
        migrations.CreateModel(
            name='Diplomados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_diplomado', models.CharField(max_length=20)),
                ('capacidad', models.IntegerField(max_length=40)),
                ('cursos_req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artemis.cursos')),
            ],
        ),
        migrations.AddField(
            model_name='cursos',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artemis.docentes'),
        ),
    ]
