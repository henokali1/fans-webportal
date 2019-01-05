from django.shortcuts import render

# Create your views here.
def logbook(request):
    args={'msg': 'LOGBOOK'}
    return render(request, 'logbook/logbook.html', args)