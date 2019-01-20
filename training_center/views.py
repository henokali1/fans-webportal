from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mso import helper
from django.core.paginator import Paginator
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
        new_trainee.academic_qualifications = request.POST['acc_qual_1']
        new_trainee.academic_qualification_insitute = request.POST['acc_qual_inst_1']
        new_trainee.academic_qualification_year = request.POST['acc_qual_year_1']
        new_trainee.professional_qualifications = request.POST['prof_qual_1']
        new_trainee.professional_qualification_insitute = request.POST['prof_qual_inst_1']
        new_trainee.professional_qualification_year = request.POST['prof_qual_year_1']
        new_trainee.enrolled_by = request.user


        first_name = request.POST['first_name'].replace(' ', '_')
        last_name = request.POST['last_name'].replace(' ', '_')

        # Get photos
        visa_copy = request.FILES['visa_copy']
        passport_copy = request.FILES['passport_copy']
        passport_size_photo = request.FILES['passport_size_photo']

        acc_qual_cert_1 = request.FILES['acc_qual_cert_1']
        prof_qual_cert_1 = request.FILES['prof_qual_cert_1']

        fs = FileSystemStorage()
        visa_file_name = fs.save(helper.get_timestamp() + '_' + first_name + '_' + last_name + '_visa_copy' + visa_copy.name[-4:], visa_copy)
        passport_file_name = fs.save(helper.get_timestamp() + '_' + first_name + '_' + last_name + '_passport_copy' + passport_copy.name[-4:], passport_copy)
        passport_size_photo_file_name = fs.save(helper.get_timestamp() + '_' + first_name + '_' + last_name + '_passport_size_photo' + passport_size_photo.name[-4:], passport_size_photo)
        acc_qual_cert_1_file_name = fs.save(helper.get_timestamp() + '_' + first_name + '_' + last_name + '_acc_qual_cert_1_' + passport_size_photo.name[-4:], acc_qual_cert_1)
        prof_qual_cert_1_file_name = fs.save(helper.get_timestamp() + '_' + first_name + '_' + last_name + '_prof_qual_cert_1_' + passport_size_photo.name[-4:], prof_qual_cert_1)

        new_trainee.visa_copy = visa_file_name
        new_trainee.passport_copy = passport_file_name
        new_trainee.passport_size_photo = passport_size_photo_file_name
        new_trainee.academic_qualification_certificate = acc_qual_cert_1_file_name
        new_trainee.professional_qualification_certificate = prof_qual_cert_1_file_name
        
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
@login_required
def all_trainees(request, msg=''):
    all_trainees = EnrollTrainee.objects.all().order_by('-pk')

    # Pagination
    paginator = Paginator(all_trainees, 10)

    page = request.GET.get('page')
    trainees = paginator.get_page(page)

    if msg == "":
        args = {'trainees': trainees}
    else:
        args = {'trainees': trainees, 'msg': msg}
    return render(request, 'training_center/all_trainees.html', args)

# Trainee Detail
@login_required
def trainee_detail(request, pk):
    trainee = EnrollTrainee.objects.all().filter(pk=pk)
    return render(request, 'training_center/course_enrolment_form_pdf.html', {'trainee':trainee[0]})

# Edit Tranee Details
@login_required
def edit_trainee(request, pk):
    if request.method == 'POST':
        trainee = EnrollTrainee.objects.filter(pk=pk).update(
            course_details = request.POST['course_details'],
            course_date = request.POST['course_date'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            private_address = request.POST['private_address'],
            office_address = request.POST['office_address'],
            date_of_birth = request.POST['date_of_birth'],
            gender = request.POST['gender'],
            mobile_number = request.POST['mobile_number'],
            telephone_number = request.POST['telephone_number'],
            email = request.POST['email'],
            employer = request.POST['employer'],
            job_title = request.POST['job_title'],
            length_of_employment = request.POST['length_of_employment'],
            name_and_address_kin = request.POST['name_and_address_kin'],
            relationship = request.POST['relationship'],
            contact_num = request.POST['contact_num'],
            academic_qualifications = request.POST['acc_qual_1'],
            academic_qualification_insitute = request.POST['acc_qual_inst_1'],
            academic_qualification_year = request.POST['acc_qual_year_1'],
            professional_qualifications = request.POST['prof_qual_1'],
            professional_qualification_insitute = request.POST['prof_qual_inst_1'],
            professional_qualification_year = request.POST['prof_qual_year_1'],
        )

        return all_trainees(
            request,
            msg='Trainee-' + str(pk) + ' Updated Successfully!',
        )
    else:
        trainee = EnrollTrainee.objects.all().filter(pk=pk)
        args = {
            'trainee': trainee[0],
        }
        return render(request, 'training_center/edit_trainee.html', args)
