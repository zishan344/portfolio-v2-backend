# Generated by Django 5.1.4 on 2025-05-14 11:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
