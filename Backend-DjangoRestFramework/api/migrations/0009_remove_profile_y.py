# Generated by Django 4.1.7 on 2023-04-08 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Y',
        ),
    ]
