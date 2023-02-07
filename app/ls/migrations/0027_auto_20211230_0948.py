# Generated by Django 3.2.7 on 2021-12-30 01:48

from django.db import migrations, models
import django.db.models.deletion
import ls.models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0026_auto_20211230_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baklajan',
            name='t_id',
            field=models.ForeignKey(default=ls.models.Baklajan.get_default, on_delete=django.db.models.deletion.CASCADE, to='ls.vegetables', verbose_name='Культура'),
        ),
        migrations.AlterField(
            model_name='perets',
            name='t_id',
            field=models.ForeignKey(default=ls.models.Perets.get_default, on_delete=django.db.models.deletion.CASCADE, to='ls.vegetables', verbose_name='Культура'),
        ),
    ]
