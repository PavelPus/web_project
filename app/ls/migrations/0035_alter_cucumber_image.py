# Generated by Django 4.0.1 on 2022-01-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0034_rename_opyl_cucumber_vids_cucumber_veg_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cucumber',
            name='image',
            field=models.ImageField(blank=True, upload_to='ls/images/cucumber'),
        ),
    ]
