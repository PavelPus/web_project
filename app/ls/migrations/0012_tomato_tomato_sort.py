# Generated by Django 3.2.7 on 2021-12-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0011_auto_20211225_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='tomato',
            name='tomato_sort',
            field=models.CharField(blank=True, choices=[('Сорт', 'Сорт'), ('Гибрид', 'Гибрид')], max_length=50),
        ),
    ]
