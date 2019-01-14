from django.db import models


# Enroll New Trainee
class EnrollTrainee(models.Model):
    course_details = models.CharField(max_length=250, default='')
    course_date = models.CharField(max_length=50, default='')
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    private_address = models.CharField(max_length=250, default='')
    office_address = models.CharField(max_length=250, default='')
    date_of_birth = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=10, default='')
    mobile_number = models.CharField(max_length=20, default='')
    telephone_number = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=254, default='')
    employer = models.CharField(max_length=250, default='')
    job_title = models.CharField(max_length=250, default='')
    length_of_employment = models.CharField(max_length=10, default='')
    name_and_address_kin = models.CharField(max_length=250, default='')
    relationship = models.CharField(max_length=250, default='')
    contact_num = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=20, default='')
    academic_qualifications = models.CharField(max_length=250, default='')
    academic_qualification_insitute = models.CharField(max_length=250, default='')
    academic_qualification_year = models.CharField(max_length=10, default='')
    professional_qualifications = models.CharField(max_length=250, default='')
    professional_qualification_insitute = models.CharField(max_length=250, default='')
    professional_qualification_year = models.CharField(max_length=10, default='')
    enrolled_on = models.DateTimeField(auto_now=True)
    enrolled_by = models.EmailField(max_length=254, default='')

    def __str__(self):
        return str(self.pk)
