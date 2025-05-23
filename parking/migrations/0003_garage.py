# Generated by Django 5.2 on 2025-04-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_alter_user_license_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('total_capacity', models.PositiveIntegerField()),
                ('available_capacity', models.PositiveIntegerField()),
                ('opening_hours', models.TimeField()),
                ('closing_hours', models.TimeField()),
                ('no_of_floors', models.CharField(default=1, max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('price_per_hour', models.CharField(default='80', max_length=100)),
                ('price_per_month', models.CharField(default='80', max_length=100)),
                ('rating', models.CharField(default='5', max_length=100)),
            ],
        ),
    ]
