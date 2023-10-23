# Generated by Django 4.2.5 on 2023-10-23 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='detalle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='entidad',
            field=models.ForeignKey(help_text='Eliga el departamento asociado', on_delete=django.db.models.deletion.CASCADE, to='core.entidad'),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(help_text='Añada el logo del departamento', upload_to=''),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='nombre',
            field=models.CharField(help_text='Ingrese el nombre del departamento', max_length=30),
        ),
    ]
