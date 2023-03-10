# Generated by Django 4.1.4 on 2023-01-05 15:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0010_detailservice_delete_detail_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdb',
            name='booked_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 5, 15, 20, 54, 551609)),
        ),
        migrations.AddField(
            model_name='contactdb',
            name='slot_status',
            field=models.CharField(default='Pending', max_length=200),
        ),
        migrations.AddField(
            model_name='contactdb',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tech_app.registerdb'),
        ),
    ]
