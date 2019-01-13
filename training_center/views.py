from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Training Center
@login_required
def training_center(request):
    return render(request, 'training_center/training_center.html', {})

# Enroll New Trainee
@login_required
def enroll_trainee(request):
    return render(request, 'training_center/enroll_trainee.html', {})

# Admin
@login_required
def admin(request):
    return render(request, 'training_center/admin.html', {})