# Generated by Django 5.0.1 on 2024-01-03 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog3', '0002_rename_slug_blogpost_desc_remove_profile_facebook_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
