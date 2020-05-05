# Generated by Django 3.0.5 on 2020-05-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20200430_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country List', 'verbose_name_plural': 'Countries List'},
        ),
        migrations.AlterField(
            model_name='country',
            name='_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='active',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='cases',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='casesPerOneMillion',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='critical',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='deaths',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='deathsPerOneMillion',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='priority',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='recovered',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='todayCases',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='todayDeaths',
            field=models.PositiveIntegerField(default=0),
        ),
    ]