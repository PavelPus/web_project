# Generated by Django 4.0.1 on 2022-04-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0059_alter_flowers_color_alter_flowers_dlinapobegov_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowers',
            name='image',
            field=models.ImageField(blank=True, upload_to='ls/images/flowers/%Y-%m-%d'),
        ),
    ]
