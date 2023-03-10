# Generated by Django 3.2.7 on 2021-12-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0004_auto_20211223_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='tomato',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='tomato',
            name='image',
            field=models.ImageField(blank=True, upload_to='ls/static/ls/images/tomato/%Y-%m-%d'),
        ),
        migrations.AlterField(
            model_name='vegetables',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
