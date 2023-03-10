# Generated by Django 4.0.1 on 2022-01-30 03:23

from django.db import migrations, models
import django.db.models.deletion
import ls.models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0036_alter_perets_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='svekla',
            name='name',
            field=models.CharField(default='<function Svekla.get_default at 0x7fc5c4052f70> ', max_length=500, verbose_name='Сорт'),
        ),
        migrations.AlterField(
            model_name='svekla',
            name='t_id',
            field=models.ForeignKey(default=ls.models.Svekla.get_default, on_delete=django.db.models.deletion.CASCADE, to='ls.vegetables', verbose_name='Культура'),
        ),
        migrations.AlterField(
            model_name='svekla',
            name='veg_type',
            field=models.CharField(default=ls.models.Svekla.get_default, max_length=100, verbose_name='Культура'),
        ),
    ]
