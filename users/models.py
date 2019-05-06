from django.contrib.auth.models import AbstractUser
from django.db import models

# User Creation Form
class CustomUser(AbstractUser):
    # add additional fields in here
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.email

# User Account Setup Form
class SetupUserAccount(models.Model):
    email = models.EmailField(max_length=254, default='')
    id_number = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=10, default='')
    department = models.CharField(max_length=50, default='')
    job_title = models.CharField(max_length=50, default='')
    page_access = models.CharField(max_length=100, default='')
    profile_pict = models.FileField(upload_to = 'media/')

    def __str__(self):
        return self.email

# All Departments
class Department(models.Model):
    department = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.department

# All Job Titles
class JobTitle(models.Model):
    job_title = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.job_title

# Page Access
class PageAccess(models.Model):
    page = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.page

