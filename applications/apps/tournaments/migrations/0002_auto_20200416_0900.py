# Generated by Django 3.0.5 on 2020-04-16 09:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='user_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_lists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='date_of_match',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='entry_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='map',
            field=models.CharField(blank=True, choices=[('PUBG MOBILE', (('Erangle', 'Erangle'), ('Sanhok', 'Sanhok'), ('Miramer', 'Miramer'), ('Vikendi', 'Vikendi'), ('TDM : Warehouse', 'TDM : Warehouse'))), ('PUBG MOBILE LITE', (('Varenge', 'Varenge'), ('Golden', 'Woods'), ('TDM : Warehouse', 'TDM : Warehouse')))], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='match_name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='match_type',
            field=models.CharField(blank=True, choices=[('Solo', 'Solo'), ('Duo', 'Duo'), ('Squad', 'Squad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='per_kill',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournament_type',
            field=models.CharField(blank=True, choices=[('PUBG Mobile', 'PUBG Mobile'), ('PUBG Mobile Lite ', 'PUBG Mobile Lite')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='winning_prize',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
