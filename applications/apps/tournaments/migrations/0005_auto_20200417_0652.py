# Generated by Django 3.0.5 on 2020-04-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_auto_20200416_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='room_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='room_password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='slot_occupancy',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
