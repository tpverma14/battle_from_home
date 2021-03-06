# Generated by Django 3.0.5 on 2020-04-17 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(blank=True, max_length=150, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FrontPageBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.CharField(blank=True, max_length=250, null=True)),
                ('main_theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_theme', to='banner.Banner')),
            ],
        ),
    ]
