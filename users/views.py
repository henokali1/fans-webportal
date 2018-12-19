from django.shortcuts import render
from .models import (
    CustomUser,
    Department,
    JobTitle,
    PageAccess,
)

# User Account Setup
def setup_account(request):
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
        
        all_users = CustomUser.objects.all()
        all_departments = Department.objects.all()
        all_job_titles = JobTitle.objects.all()
        all_pages = PageAccess.objects.all()
        return render(
            request,
            'users/setup_account.html',
            {
                'all_users': all_users,
                'all_departments': all_departments,
                'all_job_titles': all_job_titles,
                'all_pages': all_pages,
            }
        )
    else:
        # Get all Users
        all_users = CustomUser.objects.all()
        all_departments = Department.objects.all()
        all_job_titles = JobTitle.objects.all()
        all_pages = PageAccess.objects.all()
        return render(
            request,
            'users/setup_account.html',
            {
                'all_users': all_users,
                'all_departments': all_departments,
                'all_job_titles': all_job_titles,
                'all_pages': all_pages,
            }
        )

