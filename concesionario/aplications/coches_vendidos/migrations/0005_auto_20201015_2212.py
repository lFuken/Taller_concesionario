# Generated by Django 3.1.1 on 2020-10-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coches_vendidos', '0004_auto_20201014_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coche',
            name='marca',
            field=models.CharField(choices=[('1', 'KIA'), ('3', 'MERCEDES'), ('4', 'OTRO'), ('0', 'CHEVROLET'), ('2', 'HYUNDAI')], max_length=1, verbose_name='Marca'),
        ),
    ]