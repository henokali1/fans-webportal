from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mso import helper
from .models import EnrollTrainee
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import time


# Training Center
@login_required
def training_center(request):
    return render(request, 'training_center/training_center.html', {})

# Enroll New Trainee
@login_required
def enroll_trainee(request):
    gender = helper.get_gender(request.user)
    department = helper.get_department(request.user)
    current_user_name = helper.get_full_name(request.user)
    job_title = helper.get_job_title(request.user)  
    args = {
        'current_user_name': str(current_user_name),
        'current_user_email': str(request.user),
        'current_user_gender': str(gender),
        'department': str(department),
        'job_title': str(job_title),
    } 

    if request.method == 'POST':
        new_trainee = EnrollTrainee()

        new_trainee.course_details = request.POST['course_details']
        new_trainee.course_date = request.POST['course_date']
        new_trainee.first_name = request.POST['first_name']
        new_trainee.last_name = request.POST['last_name']
        new_trainee.private_address = request.POST['private_address']
        new_trainee.office_address = request.POST['office_address']
        new_trainee.date_of_birth = request.POST['date_of_birth']
        new_trainee.gender = request.POST['gender']
        new_trainee.mobile_number = request.POST['mobile_number']
        new_trainee.telephone_number = request.POST['telephone_number']
        new_trainee.email = request.POST['email']
        new_trainee.employer = request.POST['employer']
        new_trainee.job_title = request.POST['job_title']
        new_trainee.length_of_employment = request.POST['length_of_employment']
        new_trainee.name_and_address_kin = request.POST['name_and_address_kin']
        new_trainee.relationship = request.POST['relationship']
        new_trainee.contact_num = request.POST['contact_num']
        new_trainee.country = request.POST['country']
        new_trainee.academic_qualifications = request.POST['academic_qualifications']
        new_trainee.academic_qualification_insitute = request.POST['academic_qualification_insitute']
        new_trainee.academic_qualification_year = request.POST['academic_qualification_year']
        new_trainee.professional_qualifications = request.POST['professional_qualifications']
        new_trainee.professional_qualification_insitute = request.POST['professional_qualification_insitute']
        new_trainee.professional_qualification_year = request.POST['professional_qualification_year']
        new_trainee.enrolled_by = request.user


        first_name = request.POST['first_name'].replace(' ', '_')
        last_name = request.POST['last_name'].replace(' ', '_')

        # Get photos
        visa_copy = request.FILES['visa_copy']
        passport_copy = request.FILES['passport_copy']
        passport_size_photo = request.FILES['passport_size_photo']

        fs = FileSystemStorage()
        visa_file_name = fs.save(helper.get_timestamp() + '_' + first_name + '_' + last_name + '_visa_copy' + visa_copy.name[-4:], visa_copy)
        passport_file_name = fs.save(helper.get_timestamp() + '_' + first_name + '_' + last_name + '_passport_copy' + passport_copy.name[-4:], passport_copy)
        passport_size_photo_file_name = fs.save(helper.get_timestamp() + '_' + first_name + '_' + last_name + '_passport_size_photo' + passport_size_photo.name[-4:], passport_size_photo)
        
        new_trainee.visa_copy = visa_file_name
        new_trainee.passport_copy = passport_file_name
        new_trainee.passport_size_photo = passport_size_photo_file_name

        # Commit to DB
        new_trainee.save()

        return render(request, 'training_center/enroll_trainee.html', args)
    else:  
        return render(request, 'training_center/enroll_trainee.html', args)

# Training Center Admin Dashboard
@login_required
def admin(request):
    return render(request, 'training_center/admin.html', {})

# All Trainees
def all_trainees(request):
    return render(request, 'training_center/all_trainees.html', {})

# trainee_detail
def trainee_detail(request, pk):
    trainee = EnrollTrainee.objects.all().filter(pk=pk)
    return render(request, 'training_center/trainee_detail.html', {'trainee':trainee[0]})