from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from mso.helper import get_full_name


# New Logbook data
@login_required
def new_log(request):
    if request.method == 'POST':
        new_log = NewLog()

        new_log.posted_by = request.user
        new_log.posted_by_name = get_full_name(request.user)
        new_log.date = request.POST['date']
        new_log.time = request.POST['time']
        new_log.logbook_name = request.POST['logbook_name']
        new_log.description = request.POST['description']

        # Commit to Database
        new_log.save()

        args = {
            'msg': 'Data Logged Successfully!'
        }
        return render(request, 'logbook/new_log.html', args)

    else:
        # Get list of all logbooks
        args={
            'all_logbook_names':  LogbookName.objects.all(),
        }

        return render(request, 'logbook/new_log.html', args)


# All Logs
@login_required
def all_logs(request):
    args={}
    return render(request, 'logbook/all_logs.html', args)