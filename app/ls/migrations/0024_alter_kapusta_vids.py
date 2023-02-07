# Generated by Django 3.2.7 on 2021-12-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0023_kapusta_vids_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kapusta',
            name='vids',
            field=models.CharField(blank=True, choices=[('Белокочанная', 'Белокочанная'), ('Цветная', 'Цветная'), ('Брокколи', 'Брокколи'), ('Пекинская', 'Пекинская'), ('Кольраби', 'Кольраби'), ('Краснокочанная', 'Краснокочанная'), ('Савойская', 'Савойская')], max_length=50, verbose_name='Вид капусты'),
        ),
    ]
