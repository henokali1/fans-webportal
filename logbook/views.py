from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from mso.helper import get_full_name, get_department, get_job_title


# All Logs
@login_required
def all_logs(request, msg=''):
    args={
        'msg': msg,
        'department': get_department(request.user),
        'job_title': get_job_title(request.user),
        'logs': NewLog.objects.all().order_by('-pk'),
    }
    return render(request, 'logbook/all_logs.html', args)


# New Logbook data
@login_required
def new_log(request):
    if request.method == 'POST':
        new_log = NewLog()

        new_log.posted_by = request.user
        new_log.posted_by_name = get_full_name(request.user)
        new_log.logbook_name = request.POST['logbook_name']
        new_log.description = request.POST['description']

        # Commit to Database
        new_log.save()

        msg = 'Data Logged Successfully!'

        return all_logs(request, msg)

    else:
        # Get list of all logbooks
        args={
            'all_logbook_names':  LogbookName.objects.all(),
            'department': get_department(request.user),
            'job_title': get_job_title(request.user),
        }

        return render(request, 'logbook/new_log.html', args)

