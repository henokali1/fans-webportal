from django.shortcuts import render
from .models import LogbookName


# New Logbook data
def new_logbook(request):
    

    # Get list of all logbooks
    all_logbook_names = LogbookName.objects.all()
    # Extract full name only
    args={
        'all_logbook_names': all_logbook_names,
    }

    return render(request, 'logbook/new_logbook.html', args)

