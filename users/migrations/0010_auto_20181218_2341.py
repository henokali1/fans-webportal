# Generated by Django 2.1.4 on 2018-12-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20181218_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileOption',
        ),
    ]
