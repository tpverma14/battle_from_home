# Generated by Django 3.0.5 on 2020-04-18 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'default_permissions': (), 'permissions': (('view_user', 'Can view users.'), ('list_user', 'Can list users.'), ('add_user', 'Can add users.'), ('edit_user', 'Can edit users.'), ('delete_user', 'Can delete users.'), ('csv_for_user', 'Can download csv for users.'))},
        ),
    ]