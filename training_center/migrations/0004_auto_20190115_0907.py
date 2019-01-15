# Generated by Django 2.1.4 on 2019-01-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_center', '0003_auto_20190115_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolltrainee',
            name='visa_copy_photo',
        ),
        migrations.AddField(
            model_name='enrolltrainee',
            name='passport_copy',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='enrolltrainee',
            name='passport_size_photo',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='enrolltrainee',
            name='visa_copy',
            field=models.CharField(default='', max_length=250),
        ),
    ]
