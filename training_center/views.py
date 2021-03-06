from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from helper import g_drive as gd
from users.models import *
from mso import helper
from .models import *
import datetime
import time
import os


# Material Icons
def icons(request):
    return render(request, 'training_center/icons.html', {})

# Training Center
@login_required
def training_center(request):
    args={
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/training_center.html', args)

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
        'pk': helper.get_user_pk(request.user),
        'current_user_name': str(current_user_name),
        'current_user_email': str(request.user),
        'current_user_gender': str(gender),
        'department': str(department),
        'job_title': str(job_title),
        'courses': courses,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
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
    args = {
        'pk': helper.get_user_pk(request.user),
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/admin.html', args)

# All Trainees
@login_required
def all_trainees(request, msg=''):
    all_trainees = EnrollTrainee.objects.all().order_by('-pk')

    # Pagination
    paginator = Paginator(all_trainees, 10)

    page = request.GET.get('page')
    trainees = paginator.get_page(page)

    args = {
        'pk': helper.get_user_pk(request.user),
        'trainees': trainees,
        'msg': msg,
        'job_title': helper.get_job_title(request.user),
        'department': helper.get_department(request.user),
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }

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
        args = {
            'trainees': trainees,
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'batches': ClassName.objects.all().order_by('-pk'),
        }
    else:
        args = {
            'trainees': trainees,
            'msg': msg,
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'batches': ClassName.objects.all().order_by('-pk'),
        }
    args['pk'] = helper.get_user_pk(request.user)
    args['user_detail'] = SetupUserAccount.objects.all().filter(email=request.user)[0]
    return render(request, 'training_center/approve.html', args)

# Approve applications by PK through AJAX
@login_required
def approve_application(request, pk, batch):
    replay = 'Application ' + str(pk) + ' - Accepted'
    EnrollTrainee.objects.filter(pk=pk).update(
        approval = 'Accepted',
        approval_date = datetime.datetime.now(tz=timezone.utc),
        approved_by = helper.get_full_name(request.user),
        batch = batch,
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
        'pk': helper.get_user_pk(request.user),
        'trainee': trainee[0],
        'imgs': imgs,
        'len':len(imgs),
        'checkmark':"<p>sdfg</p>",
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
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
            'pk': helper.get_user_pk(request.user),
            'trainee': trainee[0],
            'courses': courses,
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        return render(request, 'training_center/edit_trainee.html', args)

# Trainer View
@login_required
def trainer(request, msg=''):
    args = {
        'pk': helper.get_user_pk(request.user),
        'clases': ClassName.objects.all().order_by('-pk'),
        'subjects': Subject.objects.all().order_by('-pk'),
        'msg': msg,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    
    return render(request, 'training_center/attendance.html', args) 

# Take Attendance
@login_required
def take_attendance(request, batch, subject_name):
    if request.method == 'POST':
        ident = str(time.time())
        for key in request.POST:
            if 'attendance' in key:
                # Attendance Status (Present, Absent, Excused, Late)
                value = request.POST[key]

                attendance = TraineeAttendance()
                attendance.attendance_stat = value
                attendance.student_id = key[key.find('_')+1:]
                attendance.attended_class = batch
                attendance.attended_subject = subject_name
                attendance.ident = ident
                # Commit to DB
                attendance.save()      
        args={'pk': helper.get_user_pk(request.user)}      
        return redirect('/training_center/attendance/', msg='Attendance Taken Successfully')
    else:
        args = {
            'pk': helper.get_user_pk(request.user),
            'filtered_stds': helper.get_stud_lst(batch, subject_name),
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        return render(request, 'training_center/take_attendance.html', args) 


    args = {'pk': helper.get_user_pk(request.user),}
    return render(request, 'training_center/head_of_training.html', args)

# All Classes
@login_required
def all_classes(request, msg=''):
    classes = ClassName.objects.all().order_by('-pk')
    args = {
        'pk': helper.get_user_pk(request.user),
        'classes': classes,
        'msg': msg,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/classes.html', args)

# Create new class (by head of training)
@login_required
def create_class(request):
    args = {
        'pk': helper.get_user_pk(request.user),
        'courses': helper.get_all_courses(Course.objects.all()),
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    if request.method == 'POST':
        new_class = ClassName()
        # Get New Class Data
        new_class.class_name = request.POST['class_name']
        new_class.courses = request.POST['course_name']
        # Commit to DB
        new_class.save()

        return all_classes(request, msg=request.POST['class_name'] + ' Added Successfully')
    else:
        return render(request, 'training_center/create_class.html', args)

# Edit Classes
@login_required
def edit_class(request, pk):
    if request.method == 'POST':        
        ClassName.objects.filter(pk=pk).update(
            class_name = request.POST['class_name'],
            courses = request.POST['course_name']
        )

        args = {
            'pk': helper.get_user_pk(request.user),
            'courses': helper.get_all_courses(Course.objects.all()),
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        return redirect('/training_center/all_classes/', msg=str(request.POST['class_name']) + ' Updated Successfully')

    else:
        course = ClassName.objects.all().filter(pk=pk)[0]
        args = {
            'pk': helper.get_user_pk(request.user),
            'class_name': course.class_name,
            'priv_course': course.courses,
            'courses': helper.get_all_courses(Course.objects.all()),
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        return render(request, 'training_center/edit_class.html', args)

# Create New Subject
@login_required
def create_subject(request):
    if request.method == 'POST':
        new_subject = Subject()
        # Get subject data
        new_subject.subject_name = request.POST['subject_name']
        new_subject.subject_type = request.POST['subject_type']
        new_subject.subject_discription = request.POST['subject_discription']
        # Commit to DB
        new_subject.save()

        args = {
            'pk': helper.get_user_pk(request.user),
            'msg': request.POST['subject_name'] + ' Added Successfully',
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        return render(request, 'training_center/create_subject.html', args)
    else:
        args = {
            'pk': helper.get_user_pk(request.user),
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        return render(request, 'training_center/create_subject.html', args)

# All Subjects
@login_required
def all_subjects(request, msg=''):
    args = {
        'pk': helper.get_user_pk(request.user),
        'subjects': Subject.objects.all().order_by('-pk'),
        'msg': msg,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/all_subjects.html', args)

# Edit Subject
@login_required
def edit_subject(request, pk):
    if request.method == 'POST':
        Subject.objects.filter(pk=pk).update(
            subject_name = request.POST['subject_name'],
            subject_type = request.POST['subject_type'],
            subject_discription = request.POST['subject_discription'],
        )

        return redirect('/training_center/subjects/all/', msg='Subject - ' + str(pk) + ' Updated Successfully.')
    else:
        args = {
            'pk': helper.get_user_pk(request.user),
            'subject': Subject.objects.all().filter(pk=pk)[0],
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        return render(request, 'training_center/edit_subject.html', args)

# Create Course
@login_required
def create_course(request):
    args = {
        'pk': helper.get_user_pk(request.user),
        'subjects': Subject.objects.all().order_by('-pk'),
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    if request.method == 'POST':
        new_course = Course()
        # Get form data
        new_course.course_details = request.POST['course_details']
        new_course.course_name = request.POST['course_name']
        new_course.course_description = request.POST['course_description']
        new_course.course_subjects_pk = request.POST.getlist('course_subjects')
        # Commit to DB
        new_course.save()
        return render(request, 'training_center/create_course.html', args)
    else:
        return render(request, 'training_center/create_course.html', args)

# All Courses
@login_required
def all_courses(request, msg=''):
    args = {
        'pk': helper.get_user_pk(request.user),
        'courses': Course.objects.all().order_by('-pk'),
        'msg': msg,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/all_courses.html', args)

# Edit Course
@login_required
def edit_course(request, pk):
    if request.method == 'POST':
        Course.objects.filter(pk=pk).update(
            course_details = request.POST['course_details'],
            course_name = request.POST['course_name'],
            course_description = request.POST['course_description'],
            course_subjects_pk = request.POST.getlist('course_subjects'),
        ) 
        return redirect('/training_center/courses/all/', msg='Course Updated Successfully')
    else:
        args = {
            'pk': helper.get_user_pk(request.user),
            'course': Course.objects.all().filter(pk=pk)[0],
            'subjects': Subject.objects.all().order_by('-pk'),
            'current_user_name': helper.get_full_name(request.user),
            'current_user_email': request.user,
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        subjects = Subject.objects.all()
        subjects_pk = eval(args['course'].course_subjects_pk)
        subjects_pk_int = []
        for i in subjects_pk:
            subjects_pk_int.append(int(i))
        args['subjects_pk_int'] = subjects_pk_int
        return render(request, 'training_center/edit_course.html', args)

# VIEW ALL ATTENDANCE RECORDS OF A SPECIFIC CLASS AND SUBJECT
@login_required
def view_subject_attendance(request, batch, subject_name):
    filtered_att, sessions = helper.get_filtered_att(batch, subject_name)
    
    args={
        'filtered_att': filtered_att,
        'msg': '',
        'batch': batch,
        'subject_name': subject_name,
        'sessions': sessions,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    
    
    if len(filtered_att) == 0:
        args['msg']="No Records Found"
    
    return render(request, 'training_center/view_subject_attendance.html', args)

# View Attendance Recordes of a Given classs, Subject and Date
@login_required
def view_attendance_subj_date(request, batch, subject_name, date):
    filtered_att = helper.get_filtered_att_date(batch, subject_name, date)
    args = {
        'pk': helper.get_user_pk(request.user),
        'filtered_att': filtered_att,
        'msg': '',
        'batch': batch,
        'subject_name': subject_name,
        'date': date,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }

    if len(filtered_att) == 0:
        args['msg']="No Records Found"
        
    return render(request, 'training_center/view_attendance_subj_date.html', args)

# View Attendance Record Filtered by Class Name Only
@login_required
def view_attendance_cls(request, batch):
    filtered_att = helper.get_stud_lst_cls(batch)
    args = {
        'pk': helper.get_user_pk(request.user),
        'filtered_att': filtered_att,
        'msg': '',
        'batch': batch,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }

    if len(filtered_att) == 0:
        args['msg']="No Records Found"

    return render(request, 'training_center/view_attendance_cls.html', args)

# Dashboard 
@login_required
def dashboard(request):
    args={
        'pk': helper.get_user_pk(request.user),
        'job_title': helper.get_job_title(request.user),
        'department': helper.get_department(request.user),
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    dashboard = Dashboard.objects.all()
    fab = Fab.objects.all()
    args['dashboard'] = dashboard
    args['fab'] = fab
    return render(request, 'training_center/dashboard.html', args)

# Grades
@login_required
def grades(request, msg=''):
    args = {
        'pk': helper.get_user_pk(request.user),
        'clases': ClassName.objects.all().order_by('-pk'),
        'subjects': Subject.objects.all().order_by('-pk'),
        'msg': msg,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }

    if request.method == 'POST':
        args['batch'] = request.POST['batch']
        args['subject'] = request.POST['subject']

        exported_grades = request.FILES['txt_file'].read()

        extracted_results = helper.get_result(exported_grades.decode("utf-8"))
        if 'err' in extracted_results:
            args['msg'] = "WRONG FILE FORMAT. PLEASE EXPORT THE RESULTS FROM EXAM VIEW AND IMPORT THE FILE AGAIN."
        else:
            args['results'] = extracted_results
            args['msg'] = 'Results Imported Successfully'

            for i in extracted_results:
                new_grade = Grade()
                new_grade.subject = request.POST['subject']
                new_grade.batch = request.POST['batch']
                new_grade.trainee_pk = helper.get_trainee_pk(i)
                new_grade.value = float(extracted_results[i])
                new_grade.greaded_by = request.user
                new_grade.save()
        
        return render(request, 'training_center/import_grades.html', args)
    return render(request, 'training_center/grades.html', args)

# All Grades
@login_required
def all_grades(request, batch_name):   
    filtered_trainees =  helper.get_all_std_grades(batch_name)
    args={
        'pk': helper.get_user_pk(request.user),
        'filtered_trainees': filtered_trainees,
        'msg': '',
        'batch_name': batch_name,
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    
    if len(filtered_trainees) == 0:
        args['msg']="No Records Found"
    return render(request, 'training_center/all_grades.html', args)


# Import Grades (Exported From Exam View Text File)
@login_required
def import_grades(request):
    args={'pk': helper.get_user_pk(request.user),}
    if request.method == 'POST':
        print('post data')
    return render(request, 'training_center/import_grades.html', args)

# Trainee Grade Detail View
@login_required
def trainee_grade(request, pk, batch_name):
    subject_grades = helper.get_course_grades(pk, batch_name)
    args={
        'pk': helper.get_user_pk(request.user),
        'trainee': EnrollTrainee.objects.all().filter(pk=pk)[0],
        'id_num': helper.get_stud_id(pk),
        'overall_grade': helper.get_overall_grade(pk, batch_name),
        'subjects': subject_grades,
        'user': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    try:
        args['attendance'] = helper.get_stud_lst_cls(batch_name)[str(pk)]['per']
    except:
        args['attendance'] = 0
    
    return render(request, 'training_center/trainee_grade.html', args)

# Edit / Add Grades Manulally 
@login_required
def edit_grades(request, pk, batch_name):
    if request.method == 'POST':
        for key in request.POST:
            # Subject PK
            value = request.POST[key]
            subject_pk = key.strip('subject_pk_ident_')
            if 'subj_ident_' in key:
                grade_obj = Grade.objects.filter(
                    trainee_pk=pk,
                    batch = batch_name,
                    subject = Subject.objects.all().filter(pk=subject_pk)[0].subject_name
                )
                if len(grade_obj) == 0:
                    new_grade = Grade()
                    new_grade.subject = Subject.objects.all().filter(pk=subject_pk)[0].subject_name
                    new_grade.batch = batch_name
                    new_grade.trainee_pk = pk
                    new_grade.value = float(request.POST[key])
                    new_grade.greaded_by = request.user
                    new_grade.save()

                else:
                    grade_obj.update(value = request.POST[key])
        redirect_url = '/training_center/grade/' + str(pk) + '/' + str(batch_name) + '/'
        return redirect(redirect_url , msg='Grade Updated Successfully')
    
    subject_grades = helper.get_course_grades(pk, batch_name)
    args={
        'trainee': EnrollTrainee.objects.all().filter(pk=pk)[0],
        'id_num': helper.get_stud_id(pk),
        'overall_grade': helper.get_overall_grade(pk, batch_name),
        'subjects': subject_grades,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    try:
        args['attendance'] = helper.get_stud_lst_cls(batch_name)[str(pk)]['per']
    except:
        args['attendance'] = 0
    
    return render(request, 'training_center/edit_grades.html', args)

# Feedback
@login_required
def feedback(request):
    serveys  ={}
    all_serveys = TraineeFeedback.objects.all()
    u_batches = []
    for i in all_serveys:
        if not i.batch in u_batches:
            u_batches.append(i.batch)
            serveys[i.pk] = {
                'pk': i.pk,
                'batch': i.batch,
                'course_code': helper.get_course_name(i.batch),
                'tot': len(TraineeFeedback.objects.all().filter(batch=i.batch)),
            }
    args = {
        'pk': helper.get_user_pk(request.user),
        'all_serveys': serveys,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/feedback.html', args)

# Trainee Feedback Form
def feedback_form(request, pk, batch_name):
    args = {
        'pk': helper.get_user_pk(request.user),
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    try:
        args['corse_name'] = ClassName.objects.all().filter(class_name=batch_name)[0].courses
    except:
        args['corse_name'] = 'corse_name'
    if request.method == 'POST':
        new_feedback = TraineeFeedback()

        new_feedback.trainee_pk = pk
        new_feedback.batch = batch_name
        new_feedback.q1a = request.POST['q1']
        new_feedback.q2a = request.POST['q2']
        new_feedback.q3a = request.POST['q3']
        new_feedback.q4a = request.POST['q4']
        new_feedback.q5a = request.POST['q5']
        new_feedback.q6a = request.POST['q6']
        new_feedback.q7a = request.POST['q7']
        new_feedback.q8a = request.POST['q8']
        new_feedback.q9a = request.POST['q9']
        new_feedback.q10a = request.POST['q10']
        new_feedback.q11a = request.POST['q11']
        new_feedback.q12a = request.POST['q12']
        new_feedback.q13a = request.POST['q13']
        new_feedback.q14a = request.POST['q14']
        new_feedback.q15a = request.POST['q15']
        new_feedback.q16a = request.POST['q16']
        new_feedback.q17a = request.POST['q17']
        new_feedback.q18a = request.POST['q18']
        new_feedback.q19a = request.POST['q19']
        new_feedback.q20a = request.POST['q20']
        new_feedback.q21a = request.POST['q21']
        new_feedback.q22a = request.POST['q22']
        new_feedback.q23a = request.POST['q23']
        new_feedback.q24a = request.POST['q24']

        new_feedback.q25a = request.POST['administration_suggestions']
        new_feedback.q26a = request.POST['th_training_suggestions']
        new_feedback.q27a = request.POST['pr_training_suggestions']
        new_feedback.q28a = request.POST['constructive_training_suggestions']

        print(request.POST['q24'])
        new_feedback.save()

    return render(request, 'training_center/feedback_form.html', args)

# Trainee Feedback Thank You Page
def feedback_thank_you(request):
    args={
        'pk': helper.get_user_pk(request.user),
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/feedback_thank_you.html', args)

# Create New Survey Invitation
@login_required
def new_feedback(request):
    all_batches = ClassName.objects.all()
    batch_names = [] 
    for i in all_batches:
        batch_names.append(i.class_name)
    args = {
        'pk': helper.get_user_pk(request.user),
        'batch_names': batch_names,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/new_feedback.html', args)

# Feedback/Servey Detail
@login_required
def feedback_detail(request, batch_name):
    args={'batch': batch_name}
    ans = helper.ans_cntr(batch_name)
    args['chart_cntr'] = ans['chart_cntr']
    args['suggestions'] = ans['suggestions']
    args['rad_btn_ans'] = ans['rad_btn_ans']
    args['resp'] = helper.total_trainees(batch_name)
    args['pk'] = helper.get_user_pk(request.user)
    args['user_detail'] = SetupUserAccount.objects.all().filter(email=request.user)[0]
    return render(request, 'training_center/feedback_detail.html', args)

# Sends servey email for the given batch name
@login_required
def feedback_email(request, batch_name):
    args={
        'pk': helper.get_user_pk(request.user),
        'email_adds': helper.get_email_addresses(batch_name),
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/feedback_email.html', args)

# Certificate
@login_required
def certificate(request, msg=''):
    all_trainees = EnrollTrainee.objects.all().filter(approval="Accepted").order_by('-pk')

    args = {
        'pk': helper.get_user_pk(request.user),
        'formated_data': helper.get_all_trainee_data(),
        'msg': msg,
        'job_title': helper.get_job_title(request.user),
        'department': helper.get_department(request.user),
        'current_user_name': helper.get_full_name(request.user),
        'current_user_email': request.user,
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    return render(request, 'training_center/certificate.html', args)


# Certificate Preview
@login_required
def certificate_preview(request, pk):
    trainee_details = helper.get_all_trainee_data()[int(pk)]
    overall_att = trainee_details['overall_att']
    overall_grade = trainee_details['overall_grade']
    can_print = (overall_att >= 85) and (overall_grade >= 75 )
    
    if request.method == 'POST':
        args={
            'pk': helper.get_user_pk(request.user),
            'name': request.POST['full_name'],
            'course_name': request.POST['course_name'],
            'date_from': request.POST['course_data_from'],
            'date_to': request.POST['course_date_to'],
            'hrs_training': request.POST['hours'],
            'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
        }
        
        return render(request, 'training_center/certificate_pdf.html', args)
    else:
        details = helper.get_cet_preview_details(pk)
        details['can_print'] = can_print
        return render(request, 'training_center/certificate_preview.html', details)

# List of Courses(Course Materials)
@login_required
def courses_list(request):
    courses = helper.get_all_courses(Course.objects.all())
    print(courses)
    args = {
        'courses': courses,
    }
    return render(request, 'training_center/list_courses.html', args)

# List of Subjects(Course Materials)
@login_required
def subjects_list(request, course):
    subjects = helper.get_subjects(course)
    args = {
        'subjects': subjects,
    }
    return render(request, 'training_center/list_subjects.html', args)

# List Course Materials of a Given Subject
@login_required
def list_course_mat(request, course, subject):
    course_materials = helper.get_course_material(subject)
    args = {'course_materials': course_materials}
    return render(request, 'training_center/list_course_mat.html', args)

# Renders(embeds) the given course material from google drive
@login_required
def render_course_mat(request, course, subject, file_name):
    drive_url = helper.get_drive_url(course, subject, file_name)
    print(drive_url)
    args = {'drive_url': drive_url}
    return render(request, 'training_center/render_course_mat.html', args)

# Upload Course Material
@login_required
def add_course_mat(request):
    args = {
        'courses': Course.objects.all().order_by('-pk'),
        'subjects': Subject.objects.all().order_by('-pk'),
        'msg': '',
    }
    if request.method == 'POST':
        fs = FileSystemStorage()

        subject = request.POST['subject']
        # cou_mat_file = request.FILES['cou_mat_file'].read()

        cou_mat_file = request.FILES['cou_mat_file']
        cou_mat_file_name = fs.save(cou_mat_file.name, cou_mat_file)

        # Save to Google Drive
        drive_file_id = gd.save_on_drive(cou_mat_file_name)
        drive_url = "https://drive.google.com/file/d/" + drive_file_id + "/preview"
        print(drive_url)

        # Delete File from Local Disk
        os.remove('/home/ubuntu/fansWebportalEnv/fans-webportal/media/' + cou_mat_file_name)

        # Save Lables on DB
        course_mat_db = CourseMaterial()

        course_mat_db.subject = Subject.objects.all().filter(subject_name=subject)[0]
        course_mat_db.file_name = cou_mat_file_name
        course_mat_db.drive_url = drive_url
        course_mat_db.drive_file_id = drive_file_id
        course_mat_db.save()
        args['msg'] = 'Course Material Added Successfully'

    return render(request, 'training_center/add_course_mat.html', args)

def a(request):
    args={}
    return render(request, 'training_center/a.html', args)
