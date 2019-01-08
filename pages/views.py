from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'

def fans_index(request):
    return render(request, 'pages/fans_index.html')

# Who we are
def who_we_are(request):
    return render(request, 'pages/who_we_are.html')

# Training center
def training_center(request):
    return render(request, 'pages/training_center.html')

# Services(ATS)
def services_ats(request):
    return render(request, 'pages/services_ats.html')

# Services(Engineering)
def services_engineering(request):
    return render(request, 'pages/services_engineering.html')

# Photo Gallery
def photo_gallery(request):
    return render(request, 'pages/photo_gallery.html')
