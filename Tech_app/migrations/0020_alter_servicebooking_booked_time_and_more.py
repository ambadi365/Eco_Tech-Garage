# Generated by Django 4.1.2 on 2023-01-08 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0019_remove_servicebooking_service_detail_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicebooking',
            name='booked_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 8, 16, 50, 7, 715401)),
        ),
        migrations.DeleteModel(
            name='DetailService',
        ),
    ]
