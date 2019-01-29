from django.db import models


# Course
class Course(models.Model):
    course_details = models.CharField(max_length=250, default='')
    course_name = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.course_name + ' - ' + self.course_details



# Class
class ClassName(models.Model):
    class_name = models.CharField(max_length=250, default='')
    courses = models.CharField(max_length=250, default='')
    courses_list = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.class_name


# Subjects
class SubjectName(models.Model):
    subject_name = models.CharField(max_length=250, default='')


# Enroll New Trainee
class EnrollTrainee(models.Model):
    course_details = models.CharField(max_length=250, default='')
    course_name = models.CharField(max_length=250, default='')
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
    academic_qualifications_two = models.CharField(max_length=250, default='')
    academic_qualification_insitute_two = models.CharField(max_length=250, default='')
    academic_qualification_year_two = models.CharField(max_length=10, default='')
    academic_qualifications_three = models.CharField(max_length=250, default='')
    academic_qualification_insitute_three = models.CharField(max_length=250, default='')
    academic_qualification_year_three = models.CharField(max_length=10, default='')
    academic_qualifications_four = models.CharField(max_length=250, default='')
    academic_qualification_insitute_four = models.CharField(max_length=250, default='')
    academic_qualification_year_four = models.CharField(max_length=10, default='')
    academic_qualifications_five = models.CharField(max_length=250, default='')
    academic_qualification_insitute_five = models.CharField(max_length=250, default='')
    academic_qualification_year_five = models.CharField(max_length=10, default='')

    professional_qualifications = models.CharField(max_length=250, default='')
    professional_qualification_insitute = models.CharField(max_length=250, default='')
    professional_qualification_year = models.CharField(max_length=10, default='')
    professional_qualifications_two = models.CharField(max_length=250, default='')
    professional_qualification_insitute_two = models.CharField(max_length=250, default='')
    professional_qualification_year_two = models.CharField(max_length=10, default='')
    professional_qualifications_three = models.CharField(max_length=250, default='')
    professional_qualification_insitute_three = models.CharField(max_length=250, default='')
    professional_qualification_year_three = models.CharField(max_length=10, default='')
    professional_qualifications_four = models.CharField(max_length=250, default='')
    professional_qualification_insitute_four = models.CharField(max_length=250, default='')
    professional_qualification_year_four = models.CharField(max_length=10, default='')
    professional_qualifications_five = models.CharField(max_length=250, default='')
    professional_qualification_insitute_five = models.CharField(max_length=250, default='')
    professional_qualification_year_five = models.CharField(max_length=10, default='')

    enrolled_on = models.DateTimeField(auto_now=True)
    enrolled_by = models.EmailField(max_length=254, default='')
    visa_copy = models.ImageField(upload_to = 'media/')
    passport_copy = models.ImageField(upload_to = 'media/')
    passport_size_photo = models.ImageField(upload_to = 'media/')

    academic_qualification_certificate = models.FileField(upload_to = 'media/')
    academic_qualification_certificate_two = models.FileField(upload_to = 'media/')
    academic_qualification_certificate_three = models.FileField(upload_to = 'media/')
    academic_qualification_certificate_four = models.FileField(upload_to = 'media/')
    academic_qualification_certificate_five = models.FileField(upload_to = 'media/')

    professional_qualification_certificate = models.FileField(upload_to = 'media/')
    professional_qualification_certificate_two = models.FileField(upload_to = 'media/')
    professional_qualification_certificate_three = models.FileField(upload_to = 'media/')
    professional_qualification_certificate_four = models.FileField(upload_to = 'media/')
    professional_qualification_certificate_five = models.FileField(upload_to = 'media/')

    approval = models.CharField(max_length=50, default='Approval Pending')
    approval_date = models.DateTimeField(auto_now=False, null=True)
    approved_by = models.CharField(max_length=250, default='')

    def __str__(self):
        return str(self.pk) + ' - ' + self.first_name.capitalize() + ' ' + self.last_name.capitalize()
