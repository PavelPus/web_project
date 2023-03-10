# Generated by Django 3.2.7 on 2021-12-27 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0015_alter_tomato_t_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lifetime', models.CharField(max_length=50, verbose_name='Время жизни')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='ls/images/%Y-%m-%d')),
            ],
            options={
                'verbose_name': 'Цветы',
                'verbose_name_plural': 'Цветы',
            },
        ),
        migrations.CreateModel(
            name='Flowers_sorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Сорт')),
                ('f_id', models.ForeignKey(default='Однолетние', on_delete=django.db.models.deletion.CASCADE, to='ls.flowers', verbose_name='Время жизни')),
            ],
        ),
    ]
