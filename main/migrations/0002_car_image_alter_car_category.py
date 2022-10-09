# Generated by Django 4.1.2 on 2022-10-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_car'),
        ),
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('1', 'Autos'), ('2', 'Pickups y Comerciales'), ('3', 'SUVs y Crossovers')], default='1', max_length=64),
        ),
    ]
