# Generated by Django 3.1.1 on 2020-10-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coches_vendidos', '0006_auto_20201015_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coche',
            name='marca',
            field=models.CharField(choices=[('2', 'HYUNDAI'), ('4', 'OTRO'), ('1', 'KIA'), ('3', 'MERCEDES'), ('0', 'CHEVROLET')], max_length=1, verbose_name='Marca'),
        ),
    ]
