# Generated by Django 2.1.4 on 2019-01-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_center', '0002_enrolltrainee_visa_copy_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolltrainee',
            name='visa_copy_photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
