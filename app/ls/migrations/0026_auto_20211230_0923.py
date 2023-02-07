# Generated by Django 3.2.7 on 2021-12-30 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0025_auto_20211229_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='perets',
            name='vids',
            field=models.CharField(blank=True, choices=[('Сладкий', 'Сладкий'), ('Острый', 'Острый')], max_length=50, verbose_name='Вид перца'),
        ),
        migrations.AddField(
            model_name='perets',
            name='vids_image',
            field=models.CharField(default='ls/images/perets/noimage.jpg', max_length=100),
        ),
    ]
