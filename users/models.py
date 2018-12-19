from django.contrib.auth.models import AbstractUser
from django.db import models

# User Creation Form
class CustomUser(AbstractUser):
    # add additional fields in here
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.email

# User Profile Setup Form
class SetupUserProfile(models.Model):
    id_number = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=10, default='')
    department = models.CharField(max_length=50, default='')
    job_title = models.CharField(max_length=50, default='')
    page_access = models.TextField(default='')