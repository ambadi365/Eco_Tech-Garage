# Generated by Django 4.1.2 on 2023-01-11 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0025_alter_servicebooking_booked_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicebooking',
            name='booked_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 6, 57, 29, 534000)),
        ),
    ]