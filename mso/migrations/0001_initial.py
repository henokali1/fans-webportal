# Generated by Django 2.1.4 on 2018-12-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cns_mso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_by', models.CharField(default='', max_length=100)),
                ('section', models.CharField(default='', max_length=100)),
                ('department_head', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('description_of_service', models.TextField(default='')),
                ('tsm_approval', models.BooleanField(default=False)),
                ('tsm_approval_date', models.DateTimeField()),
                ('actual_work_descripition', models.TextField(default='')),
                ('date_started', models.CharField(default='', max_length=50)),
                ('date_compleated', models.CharField(default='', max_length=50)),
                ('work_compleated_by', models.TextField(default='')),
                ('id_number', models.CharField(default='', max_length=254)),
                ('supervisor_approval', models.BooleanField(default=False)),
                ('supervisor_approval_date', models.DateTimeField()),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('posted_by', models.EmailField(default='', max_length=254)),
                ('requested_by_other_department', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]