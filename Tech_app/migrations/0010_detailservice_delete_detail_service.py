# Generated by Django 4.1.4 on 2023-01-05 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tech_app', '0009_detail_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_detail_name', models.CharField(blank=True, max_length=200, null=True)),
                ('time_required', models.IntegerField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tech_app.service')),
            ],
        ),
        migrations.DeleteModel(
            name='Detail_service',
        ),
    ]
