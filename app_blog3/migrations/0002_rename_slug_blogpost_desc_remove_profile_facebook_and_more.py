# Generated by Django 5.0.1 on 2024-01-03 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog3', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='slug',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linkedin',
        ),
    ]
