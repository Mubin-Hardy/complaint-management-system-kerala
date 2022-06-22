# Generated by Django 4.0.5 on 2022-06-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0011_remove_request_vehicle_name_request_vehicle_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='work_category',
            field=models.CharField(choices=[('KSEB', 'KSEB'), ('WATER AUTHORITY', 'WATER AUTHORITY')], default='KSEB', max_length=50),
            preserve_default=False,
        ),
    ]
