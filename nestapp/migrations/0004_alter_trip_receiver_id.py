# Generated by Django 4.0.3 on 2022-03-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nestapp', '0003_location_remove_trip_receiver_trip_receiver_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='receiver_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]