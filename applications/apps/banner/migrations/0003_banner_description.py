# Generated by Django 3.0.5 on 2020-04-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_auto_20200421_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
