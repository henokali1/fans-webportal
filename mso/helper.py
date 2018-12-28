from users.models import CustomUser, SetupUserAccount


# Returns full name of a give user(emal)
def get_full_name(email):
    first_name = CustomUser.objects.values_list('first_name', flat=True).filter(email=email)[0].lower()
    last_name = CustomUser.objects.values_list('last_name', flat=True).filter(email=email)[0].lower()    
    return first_name.capitalize() + ' ' + last_name.capitalize()

# Returns job title of a give user(emal)
def get_job_title(email):
    job_title = SetupUserAccount.objects.values_list('job_title', flat=True).filter(email=email)[0]
    return job_title
