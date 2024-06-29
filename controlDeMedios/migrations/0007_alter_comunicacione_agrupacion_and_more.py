# Generated by Django 5.0.4 on 2024-06-29 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlDeMedios', '0006_especialidades_delete_especialidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicacione',
            name='agrupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlDeMedios.agrupaciones'),
        ),
        migrations.AlterField(
            model_name='informatica',
            name='agrupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlDeMedios.agrupaciones'),
        ),
        migrations.AlterField(
            model_name='utilesyherramienta',
            name='agrupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlDeMedios.agrupaciones'),
        ),
    ]