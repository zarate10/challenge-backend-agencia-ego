# Generated by Django 4.1.2 on 2022-10-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_car_image_alter_car_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
