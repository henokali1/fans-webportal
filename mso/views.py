from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from users.models import SetupUserAccount, CustomUser
from . import helper
from .models import MsoCns
import ast
import datetime

# All MSO's
@login_required
def all_msos(request, msg=''):
    all_msos = MsoCns.objects.all().order_by('-pk')
    current_user_name = helper.get_full_name(request.user)   

    # Pagination
    paginator = Paginator(all_msos, 10)

    page = request.GET.get('page')
    msos = paginator.get_page(page)
    gender = helper.get_gender(request.user)
    department = helper.get_department(request.user)
    job_title = helper.get_job_title(request.user)
    args = {
        'msos': msos,
        'current_user_name': str(current_user_name),
        'current_user_email': str(request.user),
        'current_user_gender': str(gender),
        'department': str(department),
        'job_title': str(job_title),
        'msg': msg,
    }

    return render(request, 'mso/all_msos.html', args)


# New MSO
@login_required
def new_mso(request):
    # Get list of CNS staff (Engineers, Technicians...)
    all_cns_staff = list(SetupUserAccount.objects.values_list('email', flat=True).filter(department="CNS"))
    # Extract full name only
    full_names = [helper.get_full_name(email) for email in all_cns_staff]
    if request.method == 'POST':
        new_mso = MsoCns()

        new_mso.requested_by=request.POST['requested_by']
        new_mso.section = request.POST['section']
        new_mso.department_head = request.POST['department_head']
        new_mso.location = request.POST['location']
        new_mso.description_of_service = request.POST['description_of_service']
        new_mso.actual_work_descripition = request.POST['actual_work_descripition']
        new_mso.date_started = request.POST['date_started']
        new_mso.date_completed = request.POST['date_completed']
        new_mso.work_compleated_by = request.POST.getlist('work_compleated_by')
        new_mso.posted_by = request.user
        new_mso.posted_by_name = helper.get_full_name(request.user)

        # Commit to Database
        new_mso.save()
        return all_msos(request, msg='MSO Created Successfully!')
    else:       
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
            'full_names':full_names,
        }           
        return render(request, 'mso/new_mso.html', args)


# MSO Detail
@login_required
def mso(request, pk):
    mso = MsoCns.objects.all().filter(pk=pk)
    return render(request, 'mso/mso_detail.html', {'mso': mso[0]})


# MSO Edit
@login_required
def edit_mso(request, pk):
    if request.method == 'POST':
        mso = MsoCns.objects.filter(pk=pk).update(
            requested_by=request.POST['requested_by'],
            section = request.POST['section'],
            department_head = request.POST['department_head'],
            location = request.POST['location'],
            description_of_service = request.POST['description_of_service'],
            actual_work_descripition = request.POST['actual_work_descripition'],
            date_started = request.POST['date_started'],
            date_completed = request.POST['date_completed'],
            work_compleated_by = request.POST.getlist('work_compleated_by'),
        )

        return all_msos(
            request,
            msg='MSO-' + str(pk) + ' Updated Successfully!',
        )

    else:
        # Get list of CNS staff (Engineers, Technicians...)
        all_cns_staff = list(SetupUserAccount.objects.values_list('email', flat=True).filter(department="CNS"))
        # Extract full name only
        full_names = [helper.get_full_name(email) for email in all_cns_staff]
        mso = MsoCns.objects.all().filter(pk=pk)
        return render(request, 'mso/edit_mso.html', {'mso': mso[0], 'full_names':full_names})


# Delete MSO through AJAX request
@login_required
def delete_mso(request, pk):
    MsoCns.objects.filter(pk=pk).delete()
    args = {
        'res': 'MSO-' + str(pk) + 'Deleted!',
    }
    return JsonResponse(args)


@login_required
def approve(request, msg=''):
    job_title = helper.get_job_title(request.user)
    if job_title == 'CNS Manager':
        all_msos = MsoCns.objects.all().order_by('-pk').filter(manager_approval=False)
    elif job_title == 'CNS Supervisor':
        all_msos = MsoCns.objects.all().order_by('-pk').filter(supervisor_approval=False)
    else:
        print('This is niether Manager or Supervisor account. Not authorized to approve MSO\'S')
    
    
    print(job_title)
    # Pagination
    paginator = Paginator(all_msos, 10)

    page = request.GET.get('page')
    msos = paginator.get_page(page)
    gender = helper.get_gender(request.user)
    department = helper.get_department(request.user)
    current_user_name = helper.get_full_name(request.user)
    args = {
        'msos': msos,
        'current_user_name': str(current_user_name),
        'current_user_email': str(request.user),
        'current_user_gender': str(gender),
        'department': str(department),
        'job_title': str(job_title),
        'msg': msg,
    }

    return render(request, 'mso/approve.html', args)


# Approve MSO through AJAX request
@login_required
def approve_mso(request, pk, job_title):
    if job_title == 'CNS Manager':
        mso = MsoCns.objects.filter(pk=pk).update(
            manager_approval = True,
            manager_approval_date = datetime.datetime.now(tz=timezone.utc),
        )
        print('CNS Manager approved MSO', pk)
    elif job_title == 'CNS Supervisor':
        mso = MsoCns.objects.filter(pk=pk).update(
            supervisor_approval = True,
            supervisor_approval_date = datetime.datetime.now(tz=timezone.utc),
        )       
        print('CNS Supervisor approved MSO', pk)
    else:
        print('unknown account')
    args = {
        'res': 'MSO-' + str(pk) + 'Approved!',
    }
    return JsonResponse(args)


# My MSO's
@login_required
def my_msos(request, msg=''):
    all_msos = MsoCns.objects.all().filter(posted_by=request.user).order_by('-pk')
    current_user_name = helper.get_full_name(request.user)   

    # Pagination
    paginator = Paginator(all_msos, 10)

    page = request.GET.get('page')
    msos = paginator.get_page(page)
    gender = helper.get_gender(request.user)
    department = helper.get_department(request.user)
    job_title = helper.get_job_title(request.user)
    args = {
        'msos': msos,
        'current_user_name': str(current_user_name),
        'current_user_email': str(request.user),
        'current_user_gender': str(gender),
        'department': str(department),
        'job_title': str(job_title),
        'msg': msg,
    }
    return render(request, 'mso/my_msos.html', args)


# MSO Preview
@login_required
def mso_preview(request, pk, mso=''):
    mso = MsoCns.objects.all().filter(pk=pk)
    work_compleated_by_list = (ast.literal_eval(mso[0].work_compleated_by))
    work_compleated_by_names = ''

    for i in work_compleated_by_list:
        work_compleated_by_names += i + ', '
    print(work_compleated_by_names[0:-2])
    
    args={
        'mso': mso[0],
        'work_compleated_by_names': work_compleated_by_names[0:-2],
    }
    return render(request, 'mso/mso_preview.html', args)
