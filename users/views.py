from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import (
    SetupUserAccount,
    CustomUser,
    Department,
    JobTitle,
    PageAccess,
)


# User Account Setup
@login_required
def setup_account(request):
    # Get users, departments, job titles and pages
    all_users = CustomUser.objects.all()
    all_departments = Department.objects.all()
    all_job_titles = JobTitle.objects.all()
    all_pages = PageAccess.objects.all()

    if request.method == 'POST':
        # Get all users email
        all_accounts_email = list(SetupUserAccount.objects.all().values_list('email', flat=True))

        # Get current users email
        email = request.POST['email']

        # Check if this account is already setup
        if email in all_accounts_email:
            print('Existing Account')
        else:
            new_account_setup = SetupUserAccount(
                email=email,
                gender=request.POST['gender'],
                id_number=request.POST['id_number'],
                department=request.POST['department'],
                job_title=request.POST['job_title'],
                page_access=request.POST.getlist('access')
            )

            new_account_setup.save()
        
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
