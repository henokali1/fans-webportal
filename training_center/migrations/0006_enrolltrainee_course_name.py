# Generated by Django 2.1.4 on 2019-01-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_center', '0005_auto_20190121_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolltrainee',
            name='course_name',
            field=models.CharField(default='', max_length=250),
        ),
    ]