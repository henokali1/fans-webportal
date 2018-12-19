from django.shortcuts import render


def all_msos(request):
    context = {'data': 'data from server'}
    return render(request, 'mso/all_msos.html', context)

def approve(request):
    context = {'data': 'data from server'}
    return render(request, 'mso/approve.html', context)
