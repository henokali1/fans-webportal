from allauth.account.adapter import DefaultAccountAdapter
from .models import SetupUserAccount


# User job title
def get_job_title(email):
    try:
        return SetupUserAccount.objects.filter(email=email).values('job_title')[0]['job_title']
    except:
        return -1

# User department
def get_department(email):
    try:
        return SetupUserAccount.objects.filter(email=email).values('department')[0]['department']
    except:
        return -1

# Redirect URL
def get_redirect_url(email):
    job_title = get_job_title(email)
    department = get_department(email)
    print(department, 'department')
    print(job_title,'job_title')
    if (job_title or department) == (-1):
        return '/user/setup-account/'
    elif (department == 'Admin'):
        return('/training_center/trainee/all/')
    elif (job_title == 'Head of Training'):
        return('/training_center/trainee/approve/')
    elif department == 'CNS':
        if job_title in ['CNS Manager', 'CNS Chief Engineer', 'CNS Supervisor']:
            return '/mso/approve/'
        elif job_title in ['CNS Engineer', 'CNS Technician', 'CNS Helper']:
            return '/mso/'
        else:
            return '/user/setup-account/'
    else:
        return '/training_center/'

class AccountAdapter(DefaultAccountAdapter): 
    def get_login_redirect_url(self, request):
        #url = super(AccountAdapter, self).get_login_redirect_url(request)
        user = request.user
        url = get_redirect_url(user)
        print(url, 'redirect url')
        return url
