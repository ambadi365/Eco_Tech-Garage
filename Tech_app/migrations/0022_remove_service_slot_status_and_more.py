# Generated by Django 4.1.2 on 2023-01-08 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0021_servicestatusdetail_payment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='slot_status',
        ),
        migrations.AlterField(
            model_name='servicebooking',
            name='booked_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 8, 19, 4, 31, 87119)),
        ),
    ]