# Generated by Django 2.1.4 on 2018-12-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181218_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alldepartments',
            name='department_list',
        ),
        migrations.AddField(
            model_name='alldepartments',
            name='department_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
