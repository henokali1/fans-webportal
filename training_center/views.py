from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from mso import helper
from django.core.paginator import Paginator
from .models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import time
import json
from django.utils import timezone
import datetime



# Training Center
@login_required
def training_center(request):
    return render(request, 'training_center/training_center.html', {})

# Enroll New Trainee
@login_required
def enroll_trainee(request):
    # Get courses dict
    courses = helper.get_all_courses(Course.objects.all()) 
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
        'courses': courses,
    } 

    if request.method == 'POST':
        new_trainee = EnrollTrainee()
        course = request.POST['course_details']
        new_trainee.course_name = course
        new_trainee.course_details = courses[course]
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
        new_trainee.academic_qualifications_two = request.POST['acc_qual_2']
        new_trainee.academic_qualifications_three = request.POST['acc_qual_3']
        new_trainee.academic_qualifications_four = request.POST['acc_qual_4']
        new_trainee.academic_qualifications_five = request.POST['acc_qual_5']
        new_trainee.academic_qualification_insitute = request.POST['acc_qual_inst_1']
        new_trainee.academic_qualification_insitute_two = request.POST['acc_qual_inst_2']
        new_trainee.academic_qualification_insitute_three = request.POST['acc_qual_inst_3']
        new_trainee.academic_qualification_insitute_four = request.POST['acc_qual_inst_4']
        new_trainee.academic_qualification_insitute_five = request.POST['acc_qual_inst_5']
        new_trainee.academic_qualification_year = request.POST['acc_qual_year_1']
        new_trainee.academic_qualification_year_two = request.POST['acc_qual_year_2']
        new_trainee.academic_qualification_year_three = request.POST['acc_qual_year_3']
        new_trainee.academic_qualification_year_four = request.POST['acc_qual_year_4']
        new_trainee.academic_qualification_year_five = request.POST['acc_qual_year_5']


        new_trainee.professional_qualifications = request.POST['prof_qual_1']
        new_trainee.professional_qualifications_two = request.POST['prof_qual_2']
        new_trainee.professional_qualifications_three = request.POST['prof_qual_3']
        new_trainee.professional_qualifications_four = request.POST['prof_qual_4']
        new_trainee.professional_qualifications_five = request.POST['prof_qual_5']
        new_trainee.professional_qualification_insitute = request.POST['prof_qual_inst_1']
        new_trainee.professional_qualification_insitute_two = request.POST['prof_qual_inst_2']
        new_trainee.professional_qualification_insitute_three = request.POST['prof_qual_inst_3']
        new_trainee.professional_qualification_insitute_four = request.POST['prof_qual_inst_4']
        new_trainee.professional_qualification_insitute_five = request.POST['prof_qual_inst_5']
        new_trainee.professional_qualification_year = request.POST['prof_qual_year_1']
        new_trainee.professional_qualification_year_two = request.POST['prof_qual_year_2']
        new_trainee.professional_qualification_year_three = request.POST['prof_qual_year_3']
        new_trainee.professional_qualification_year_four = request.POST['prof_qual_year_4']
        new_trainee.professional_qualification_year_five = request.POST['prof_qual_year_5']

        new_trainee.enrolled_by = request.user

        fs = FileSystemStorage()

        # Get photos
        try:
            visa_copy = request.FILES['visa_copy']
            visa_file_name = fs.save(visa_copy.name, visa_copy)
            new_trainee.visa_copy = visa_file_name
        except:
            print('Couldn\'t find visa_copy' )

        try:
            passport_copy = request.FILES['passport_copy']
            passport_file_name = fs.save(passport_copy.name, passport_copy)
            new_trainee.passport_copy = passport_file_name
        except:
            print('Couldn\'t find passport_copy' )

        try:
            passport_size_photo = request.FILES['passport_size_photo']
            passport_size_photo_file_name = fs.save(passport_size_photo.name , passport_size_photo)
            new_trainee.passport_size_photo = passport_size_photo_file_name
        except:
            print('Couldn\'t find passport_size_photo' )
        
        try:
            acc_qual_cert_1 = request.FILES['acc_qual_cert_1']
            acc_qual_cert_1_file_name = fs.save(acc_qual_cert_1.name, acc_qual_cert_1)
            new_trainee.academic_qualification_certificate = acc_qual_cert_1_file_name
        except:
            print('Couldn\'t find acc_qual_cert_1' )

        try:
            acc_qual_cert_2 = request.FILES['acc_qual_cert_2']
            acc_qual_cert_2_file_name = fs.save(acc_qual_cert_2.name, acc_qual_cert_2)
            new_trainee.academic_qualification_certificate_two = acc_qual_cert_2_file_name
        except:
            print('Couldn\'t find acc_qual_cert_2' )

        try:
            acc_qual_cert_3 = request.FILES['acc_qual_cert_3']
            acc_qual_cert_3_file_name = fs.save(acc_qual_cert_3.name, acc_qual_cert_3)
            new_trainee.academic_qualification_certificate_three = acc_qual_cert_3_file_name
        except:
            print('Couldn\'t find acc_qual_cert_3' )
        
        try:
            acc_qual_cert_4 = request.FILES['acc_qual_cert_4']
            acc_qual_cert_4_file_name = fs.save(acc_qual_cert_4.name, acc_qual_cert_4)
            new_trainee.academic_qualification_certificate_four = acc_qual_cert_4_file_name
        except:
            print('Couldn\'t find acc_qual_cert_4' )
        
        try:
            acc_qual_cert_5 = request.FILES['acc_qual_cert_5']
            acc_qual_cert_5_file_name = fs.save(acc_qual_cert_5.name, acc_qual_cert_5)
            new_trainee.academic_qualification_certificate_five = acc_qual_cert_5_file_name
        except:
            print('Couldn\'t find acc_qual_cert_5' )

        try:
            prof_qual_cert_1 = request.FILES['prof_qual_cert_1']
            prof_qual_cert_1_file_name = fs.save(prof_qual_cert_1.name, prof_qual_cert_1)
            new_trainee.professional_qualification_certificate = prof_qual_cert_1_file_name
        except:
            print('Couldn\'t find prof_qual_cert_1' )

        try:
            prof_qual_cert_2 = request.FILES['prof_qual_cert_2'] 
            prof_qual_cert_2_file_name = fs.save(prof_qual_cert_2.name, prof_qual_cert_2)   
            new_trainee.professional_qualification_certificate_two = prof_qual_cert_2_file_name  
        except:
            print('Couldn\'t find prof_qual_cert_2' )

        try:
            prof_qual_cert_3 = request.FILES['prof_qual_cert_3']
            prof_qual_cert_3_file_name = fs.save(prof_qual_cert_3.name, prof_qual_cert_3)
            new_trainee.professional_qualification_certificate_three = prof_qual_cert_3_file_name 
        except:
            print('Couldn\'t find prof_qual_cert_3' )

        try:
            prof_qual_cert_4 = request.FILES['prof_qual_cert_4']
            prof_qual_cert_4_file_name = fs.save(prof_qual_cert_4.name, prof_qual_cert_4)
            new_trainee.professional_qualification_certificate_four = prof_qual_cert_4_file_name
        except:
            print('Couldn\'t find prof_qual_cert_4' )

        try:
            prof_qual_cert_5 = request.FILES['prof_qual_cert_5']
            prof_qual_cert_5_file_name = fs.save(prof_qual_cert_5.name, prof_qual_cert_5)
            new_trainee.professional_qualification_certificate_five = prof_qual_cert_5_file_name
        except:
            print('Couldn\'t find prof_qual_cert_5' )
        
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

# Approve application
@login_required
def approve(request, msg=''):
    all_trainees = EnrollTrainee.objects.all().order_by('-pk')

    # Pagination
    paginator = Paginator(all_trainees, 10)

    page = request.GET.get('page')
    trainees = paginator.get_page(page)

    if msg == "":
        args = {'trainees': trainees}
    else:
        args = {'trainees': trainees, 'msg': msg}
    return render(request, 'training_center/approve.html', args)

# Approve applications by PK
@login_required
def approve_application(request, pk):
    replay = 'Application ' + str(pk) + ' - Accepted'
    EnrollTrainee.objects.filter(pk=pk).update(
        approval = 'Accepted',
        approval_date = datetime.datetime.now(tz=timezone.utc),
        approved_by = helper.get_full_name(request.user),
    )
    return HttpResponse(replay)

# Reject applications by PK
@login_required
def reject_application(request, pk):
    replay = 'Application ' + str(pk) + ' - Rejected'
    EnrollTrainee.objects.filter(pk=pk).update(
        approval = 'Rejected',
        approved_by = str(request.user),
    )  
    return HttpResponse(replay)

# Trainee Detail
@login_required
def trainee_detail(request, pk):
    trainee = EnrollTrainee.objects.all().filter(pk=pk)
    imgs = []
    if(trainee[0].visa_copy != ''):
        imgs.append('<img style="display: none;" id="visa_copy" src="' + trainee[0].visa_copy.url + '" alt="">')
    if(trainee[0].passport_copy != ''):
        imgs.append('<img style="display: none;" id="passport_copy" src="' + trainee[0].passport_copy.url + '" alt="">')
    if(trainee[0].passport_size_photo != ''):
        imgs.append('<img style="display: none;" id="passport_size_photo" src="' + trainee[0].passport_size_photo.url + '" alt="">')
    if(trainee[0].academic_qualification_certificate != ''):
        imgs.append('<img style="display: none;" id="academic_qualification_certificate" src="' + trainee[0].academic_qualification_certificate.url + '" alt="">')
    if(trainee[0].academic_qualification_certificate_two != ''):
        imgs.append('<img style="display: none;" id="academic_qualification_certificate_two" src="' + trainee[0].academic_qualification_certificate_two.url + '" alt="">')
    if(trainee[0].academic_qualification_certificate_three != ''):
        imgs.append('<img style="display: none;" id="academic_qualification_certificate_three" src="' + trainee[0].academic_qualification_certificate_three.url + '" alt="">')
    if(trainee[0].academic_qualification_certificate_four != ''):
        imgs.append('<img style="display: none;" id="academic_qualification_certificate_four" src="' + trainee[0].academic_qualification_certificate_four.url + '" alt="">')
    if(trainee[0].academic_qualification_certificate_five != ''):
        imgs.append('<img style="display: none;" id="academic_qualification_certificate_five" src="' + trainee[0].academic_qualification_certificate_five.url + '" alt="">')
    if(trainee[0].professional_qualification_certificate != ''):
        imgs.append('<img style="display: none;" id="professional_qualification_certificate" src="' + trainee[0].professional_qualification_certificate.url + '" alt="">')
    if(trainee[0].professional_qualification_certificate_two != ''):
        imgs.append('<img style="display: none;" id="professional_qualification_certificate_two" src="' + trainee[0].professional_qualification_certificate_two.url + '" alt="">')
    if(trainee[0].professional_qualification_certificate_three != ''):
        imgs.append('<img style="display: none;" id="professional_qualification_certificate_three" src="' + trainee[0].professional_qualification_certificate_three.url + '" alt="">')
    if(trainee[0].professional_qualification_certificate_four != ''):
        imgs.append('<img style="display: none;" id="professional_qualification_certificate_four" src="' + trainee[0].professional_qualification_certificate_four.url + '" alt="">')
    if(trainee[0].professional_qualification_certificate_five != ''):
        imgs.append('<img style="display: none;" id="professional_qualification_certificate_five" src="' + trainee[0].professional_qualification_certificate_five.url + '" alt="">')
    
    
    args = {
        'trainee': trainee[0],
        'imgs': imgs,
        'len':len(imgs),
        'checkmark':"<p>sdfg</p>",
    }
    return render(request, 'training_center/course_enrolment_form_pdf.html', args)

# Edit Tranee Details
@login_required
def edit_trainee(request, pk):
    # Get courses dict
    courses = helper.get_all_courses(Course.objects.all()) 
    if request.method == 'POST':
        course = request.POST['course_details']
        EnrollTrainee.objects.filter(pk=pk).update(
            course_details = courses[course],
            course_name = course,
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

        fs = FileSystemStorage()

        try:
            visa_copy = request.FILES['visa_copy']
            visa_file_name = fs.save(visa_copy.name, visa_copy)
            EnrollTrainee.objects.filter(pk=pk).update(visa_copy = visa_file_name)  
        except:
            print('Couldn\'t find visa_copy' )
            pass

        try:
            passport_copy = request.FILES['passport_copy']
            passport_file_name = fs.save(passport_copy.name, passport_copy)
            EnrollTrainee.objects.filter(pk=pk).update(passport_copy = passport_file_name)  
        except:
            print('Couldn\'t find passport_copy' )
            pass

        try:
            passport_size_photo = request.FILES['passport_size_photo']
            passport_size_photo_file_name = fs.save(passport_size_photo.name , passport_size_photo)
            EnrollTrainee.objects.filter(pk=pk).update(passport_size_photo = passport_size_photo_file_name)  
        except:
            print('Couldn\'t find passport_size_photo_file_name' )
            pass


        try:
            acc_qual_cert_1 = request.FILES['acc_qual_cert_1']
            acc_qual_cert_1_file_name = fs.save(acc_qual_cert_1.name, acc_qual_cert_1)
            EnrollTrainee.objects.filter(pk=pk).update(academic_qualification_certificate = acc_qual_cert_1_file_name)  
        except:
            print('Couldn\'t find acc_qual_cert_1' )
            pass

        try:
            acc_qual_cert_2 = request.FILES['acc_qual_cert_2']
            acc_qual_cert_2_file_name = fs.save(acc_qual_cert_2.name, acc_qual_cert_2)
            EnrollTrainee.objects.filter(pk=pk).update(academic_qualification_certificate_two = acc_qual_cert_2_file_name)  
        except:
            print('Couldn\'t find acc_qual_cert_2' )
            pass

        try:
            acc_qual_cert_3 = request.FILES['acc_qual_cert_3']
            acc_qual_cert_3_file_name = fs.save(acc_qual_cert_3.name, acc_qual_cert_3)
            EnrollTrainee.objects.filter(pk=pk).update(academic_qualification_certificate_three = acc_qual_cert_3_file_name)  
        except:
            print('Couldn\'t find acc_qual_cert_3' )
            pass

        try:
            acc_qual_cert_4 = request.FILES['acc_qual_cert_4']
            acc_qual_cert_4_file_name = fs.save(acc_qual_cert_4.name, acc_qual_cert_4)
            EnrollTrainee.objects.filter(pk=pk).update(academic_qualification_certificate_four = acc_qual_cert_4_file_name)  
        except:
            print('Couldn\'t find acc_qual_cert_4' )
            pass

        try:
            acc_qual_cert_5 = request.FILES['acc_qual_cert_5']
            acc_qual_cert_5_file_name = fs.save(acc_qual_cert_5.name, acc_qual_cert_5)
            EnrollTrainee.objects.filter(pk=pk).update(academic_qualification_certificate_five = acc_qual_cert_5_file_name)  
        except:
            print('Couldn\'t find acc_qual_cert_5' )
            pass

        try:
            prof_qual_cert_1 = request.FILES['prof_qual_cert_1']
            prof_qual_cert_1_file_name = fs.save(prof_qual_cert_1.name, prof_qual_cert_1)
            EnrollTrainee.objects.filter(pk=pk).update(professional_qualification_certificate = prof_qual_cert_1_file_name)  
        except:
            print('Couldn\'t find prof_qual_cert_1' )
            pass

        try:
            prof_qual_cert_2 = request.FILES['prof_qual_cert_2'] 
            prof_qual_cert_2_file_name = fs.save(prof_qual_cert_2.name, prof_qual_cert_2)   
            EnrollTrainee.objects.filter(pk=pk).update(professional_qualification_certificate_two = prof_qual_cert_2_file_name)  
        except:
            print('Couldn\'t find prof_qual_cert_2' )
            pass

        try:
            prof_qual_cert_3 = request.FILES['prof_qual_cert_3']
            prof_qual_cert_3_file_name = fs.save(prof_qual_cert_3.name, prof_qual_cert_3)
            EnrollTrainee.objects.filter(pk=pk).update(professional_qualification_certificate_three = prof_qual_cert_3_file_name)  
        except:
            print('Couldn\'t find prof_qual_cert_3' )
            pass
        
        try:
            prof_qual_cert_4 = request.FILES['prof_qual_cert_4']
            prof_qual_cert_4_file_name = fs.save(prof_qual_cert_4.name, prof_qual_cert_4)
            EnrollTrainee.objects.filter(pk=pk).update(professional_qualification_certificate_four = prof_qual_cert_4_file_name)  
        except:
            print('Couldn\'t find prof_qual_cert_4' )
            pass

        try:
            prof_qual_cert_5 = request.FILES['prof_qual_cert_5']
            prof_qual_cert_5_file_name = fs.save(prof_qual_cert_5.name, prof_qual_cert_5)
            EnrollTrainee.objects.filter(pk=pk).update(professional_qualification_certificate_five = prof_qual_cert_5_file_name)  
        except:
            print('Couldn\'t find prof_qual_cert_5' )
            pass


        return all_trainees(
            request,
            msg='Trainee-' + str(pk) + ' Updated Successfully!',
        )
    else:
        trainee = EnrollTrainee.objects.all().filter(pk=pk)
        args = {
            'trainee': trainee[0],
            'courses': courses,
        }
        return render(request, 'training_center/edit_trainee.html', args)

# Take Attendance
@login_required
def take_attendance(request):
    args={
        'msg': '',
        'trainees': EnrollTrainee.objects.all().order_by('-pk'),
    }
    return render(request, 'training_center/take_attendance.html', args) 