# Generated by Django 3.0.5 on 2020-04-21 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200421_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
