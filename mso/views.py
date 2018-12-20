from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def all_msos(request):
    context = {'data': 'data from server'}
    return render(request, 'mso/all_msos.html', context)

def approve(request):
    context = {'data': 'data from server'}
    return render(request, 'mso/approve.html', context)


# New MSO
@login_required
def new_mso(request):
    if request.method == 'POST':
        requested_by=request.POST['requested_by']
        section = request.POST['section']
        department_head = request.POST['department_head']
        location = request.POST['location']
        description_of_service = request.POST['description_of_service']
        actual_work_description = request.POST['actual_work_description']
        date_started = request.POST['date_started']
        date_completed = request.POST['date_completed']
        work_completed_by = request.POST.getlist('work_completed_by')

        lst = {
            'requested_by': requested_by,
            'section': section,
            'department_head': department_head,
            'location': location,
            'description_of_service': description_of_service,
            'actual_work_description': actual_work_description,
            'date_started':date_started,
            'date_completed': date_completed,
            'work_completed_by': work_completed_by,
        }

        for i in lst.keys():
            print(i, lst[i])
        return render(request, 'mso/new_mso.html')
    else:
        return render(request, 'mso/new_mso.html')