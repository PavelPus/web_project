# Generated by Django 3.2.7 on 2021-12-27 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0013_auto_20211226_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomato',
            name='image',
            field=models.ImageField(blank=True, upload_to='ls/images/tomato'),
        ),
        migrations.AlterField(
            model_name='tomato',
            name='t_id',
            field=models.ForeignKey(default='Томаты', on_delete=django.db.models.deletion.CASCADE, related_name='Культура', to='ls.vegetables'),
        ),
    ]