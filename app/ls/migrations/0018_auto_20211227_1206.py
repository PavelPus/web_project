# Generated by Django 3.2.7 on 2021-12-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0017_alter_flowers_sorts_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tomato',
            options={'verbose_name': 'Сорта томатов', 'verbose_name_plural': 'Сорта томатов'},
        ),
        migrations.AddField(
            model_name='tomato',
            name='tomato_form',
            field=models.CharField(blank=True, max_length=50, verbose_name='Форма плода'),
        ),
        migrations.AddField(
            model_name='tomato',
            name='tomato_goal',
            field=models.CharField(blank=True, max_length=50, verbose_name='Назначение'),
        ),
        migrations.AddField(
            model_name='tomato',
            name='tomato_grunt',
            field=models.CharField(blank=True, choices=[('Открытый грунт', 'Открытый грунт'), ('Закрытый грунт', 'Закрытый грунт')], max_length=50, verbose_name='Способ выращивания'),
        ),
        migrations.AddField(
            model_name='tomato',
            name='tomato_size',
            field=models.CharField(blank=True, max_length=50, verbose_name='Размер плода'),
        ),
        migrations.AddField(
            model_name='tomato',
            name='tomato_time',
            field=models.CharField(blank=True, max_length=50, verbose_name='Срок созревания'),
        ),
        migrations.AlterField(
            model_name='tomato',
            name='tomato_color',
            field=models.CharField(blank=True, max_length=50, verbose_name='Цвет плода'),
        ),
    ]