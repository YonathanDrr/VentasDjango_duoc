# Generated by Django 3.1.2 on 2020-11-03 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0003_curso_detallecurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(null=True, upload_to='curso'),
        ),
    ]
