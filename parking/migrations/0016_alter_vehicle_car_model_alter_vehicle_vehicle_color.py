# Generated by Django 5.1.7 on 2025-04-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0015_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='car_model',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_color',
            field=models.CharField(default='no-color', max_length=20),
        ),
    ]
