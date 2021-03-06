# Generated by Django 3.0.4 on 2020-04-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='country',
            field=models.CharField(default='', max_length=50, verbose_name='Country Name'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='countryKurdishName',
            field=models.CharField(default='', max_length=50, verbose_name='Kurdish Name'),
        ),
        migrations.AlterField(
            model_name='countries',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
        migrations.AlterField(
            model_name='countries',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
    ]
