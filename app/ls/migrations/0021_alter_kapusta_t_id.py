# Generated by Django 3.2.7 on 2021-12-27 07:08

from django.db import migrations, models
import django.db.models.deletion
import ls.models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0020_baklajan_cucumber_kapusta_morkov_perets_redis_svekla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kapusta',
            name='t_id',
            field=models.ForeignKey(default=ls.models.Kapusta.get_default, on_delete=django.db.models.deletion.CASCADE, to='ls.vegetables', verbose_name='Культура'),
        ),
    ]