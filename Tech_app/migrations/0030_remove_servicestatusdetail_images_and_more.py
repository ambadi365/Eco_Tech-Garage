# Generated by Django 4.1.2 on 2023-01-11 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0029_alter_contact_c_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicestatusdetail',
            name='images',
        ),
        migrations.AlterField(
            model_name='servicebooking',
            name='booked_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 8, 6, 38, 304126)),
        ),
    ]
