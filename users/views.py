from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.shortcuts import render
from users.models import *
from mso import helper
from .models import *

# User Account Setup
@login_required
def profile(request, pk):
    args={
        'last_name': helper.get_last_name(request.user),
        'first_name': helper.get_first_name(request.user),
        'job_title': helper.get_job_title(request.user),
        'department': helper.get_department(request.user),
        'current_user_email': request.user,
        'pk': helper.get_user_pk(request.user),
        'user_detail': SetupUserAccount.objects.all().filter(email=request.user)[0],
    }
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        CustomUser.objects.filter(email=request.user).update(
            first_name = first_name,
            last_name = last_name,
        )


        fs = FileSystemStorage()
        # Get Profile Picture
        try:
            profile_pic = request.FILES['profile_picture']
            profile_pict_file_name = fs.save(profile_pic.name, profile_pic)
            SetupUserAccount.objects.filter(email=request.user).update(
                profile_pict = profile_pict_file_name,
            )            
            #new_trainee.profile_pic = profile_pict_file_name
            print(profile_pict_file_name)
        except:
            print('Couldn\'t find Profile Pic' )
        return redirect('/training_center/dashboard/', args)
        #return render(request, 'training_center/dashboard.html', args)
        
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
                'pk': helper.get_user_pk(request.user),
                'all_users': all_users,
                'all_departments': all_departments,
                'all_job_titles': all_job_titles,
                'all_pages': all_pages,
                'user': SetupUserAccount.objects.all().filter(email=request.user)[0],
            }
        )
    else:
        return render(
            request,
            'users/setup_account.html',
            {
                'pk': helper.get_user_pk(request.user),
                'all_users': all_users,
                'all_departments': all_departments,
                'all_job_titles': all_job_titles,
                'all_pages': all_pages,
                'user': SetupUserAccount.objects.all().filter(email=request.user)[0],
            }
        )
