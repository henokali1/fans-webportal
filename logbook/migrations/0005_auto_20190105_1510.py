# Generated by Django 2.1.4 on 2019-01-05 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0004_newlog_posted_by_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newlog',
            name='date',
        ),
        migrations.RemoveField(
            model_name='newlog',
            name='time',
        ),
    ]
