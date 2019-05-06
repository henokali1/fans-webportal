from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mso import helper
from .models import *

# User Account Setup
@login_required
def profile(request, pk):
    args={
        'last_name': helper.get_last_name(request.user),
        'first_name': helper.get_first_name(request.user),
        'current_user_email': request.user,
        'pk': helper.get_user_pk(request.user)
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['current_user_email']

        # Get Profile Picture
        try:
            profile_pic = request.FILES['profile_picture']
            profile_pict_file_name = fs.save(profile_pic.name, profile_pic)
            new_trainee.profile_pic = profile_pict_file_name
            print(profile_pict_file_name)
        except:
            print('Couldn\'t find Profile Pic' )
        print(first_name, last_name, email)
        
        return render(request, 'users/profile.html', args)

    return render(request, 'users/profile.html', args)

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
