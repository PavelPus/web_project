# Generated by Django 3.2.7 on 2021-12-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0005_auto_20211223_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='tomato',
            name='tomato_type',
            field=models.CharField(blank=True, choices=[('Детерминантный', 'Детерминантный'), ('Индетерминантный', 'Индетерминантный')], max_length=50),
        ),
    ]
