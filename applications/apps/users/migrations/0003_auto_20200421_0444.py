# Generated by Django 3.0.5 on 2020-04-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200418_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ifsc_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='paytm_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='upi_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
