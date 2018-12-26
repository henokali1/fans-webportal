from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import SetupUserAccount, CustomUser
from . import helper
from .models import MsoCns


# All MSO's
@login_required
def all_msos(request):
    all_msos = MsoCns.objects.all().order_by('-pk')
    current_user_name = helper.get_full_name(request.user)
    print(current_user_name)
    args = {
        'msos': all_msos,
        'current_user_name': str(current_user_name),
         'current_user_email': str(request.user),
    }
    return render(request, 'mso/all_msos.html', args)

def approve(request):
    context = {'data': 'data from server'}
    return render(request, 'mso/approve.html', context)


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
        return redirect('/mso/all')
    else:                    
        return render(request, 'mso/new_mso.html', {'full_names':full_names})


# MSO Detail
@login_required
def mso(request, pk):
    mso = MsoCns.objects.all().filter(pk=pk)
    return render(request, 'mso/mso_detail.html', {'mso': mso[0]})