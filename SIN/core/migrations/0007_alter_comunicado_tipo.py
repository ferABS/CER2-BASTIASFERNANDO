# Generated by Django 4.2.5 on 2023-10-24 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_comunicado_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='tipo',
            field=models.CharField(choices=[('-', 'Seleccionar'), ('S', 'Suspensión de actividades'), ('C', 'Suspensión de clases'), ('I', 'Información')], default='-', max_length=20),
        ),
    ]
