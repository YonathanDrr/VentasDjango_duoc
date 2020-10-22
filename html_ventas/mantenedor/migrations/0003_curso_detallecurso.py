# Generated by Django 3.1.1 on 2020-10-22 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0002_auto_20201022_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('anio', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('autor', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('comunaFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.comuna', verbose_name='ComunaId')),
            ],
            options={
                'db_table': 'curso',
            },
        ),
        migrations.CreateModel(
            name='DetalleCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.IntegerField()),
                ('cantidadClass', models.IntegerField()),
                ('temporada', models.CharField(max_length=10)),
                ('nivel', models.CharField(max_length=15)),
                ('idioma', models.CharField(max_length=15)),
                ('codCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.curso')),
                ('codDesc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.descuento')),
            ],
            options={
                'db_table': 'detalleCurso',
            },
        ),
    ]