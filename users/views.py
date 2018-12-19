from django.shortcuts import render
from .models import CustomUser

# User Profile Setup
def setup_profile(request):
    if request.method == 'POST':
        email = request.POST['email']
        gender = request.POST['gender']
        id_number = request.POST['id_number']
        department = request.POST['department']
        job_title = request.POST['job_title']

        print(email)
        print(gender)
        print(id_number)
        print(department)
        print(job_title)
        return render(request, 'users/setup_profile.html',
            {'all_users': all_users})
    else:
        # Get all Users
        all_users = CustomUser.objects.all()
        return render(request, 'users/setup_profile.html',
            {'all_users': all_users})

