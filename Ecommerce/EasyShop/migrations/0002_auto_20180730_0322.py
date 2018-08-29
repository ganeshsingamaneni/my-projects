# Generated by Django 2.0.7 on 2018-07-30 03:22

import EasyShop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=EasyShop.models.new_file_name),
        ),
        migrations.AlterField(
            model_name='items',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=EasyShop.models.new_image_name),
        ),
    ]
