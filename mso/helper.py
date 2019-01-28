from users.models import CustomUser, SetupUserAccount
import time
import pytz


# Returns full name of a given user(emal)
def get_full_name(email):
    first_name = CustomUser.objects.values_list('first_name', flat=True).filter(email=email)[0].lower()
    last_name = CustomUser.objects.values_list('last_name', flat=True).filter(email=email)[0].lower()    
    return first_name.capitalize() + ' ' + last_name.capitalize()

# Returns job title of a given user(emal)
def get_job_title(email):
    job_title = SetupUserAccount.objects.values_list('job_title', flat=True).filter(email=email)[0]
    return job_title

# Returns gender of a given user(email)
def get_gender(email):
    gender = SetupUserAccount.objects.values_list('gender', flat=True).filter(email=email)[0]
    return gender

# Returns department of a given user(email)
def get_department(email):
    department = SetupUserAccount.objects.values_list('department', flat=True).filter(email=email)[0]
    return department    

# Returns date, time of a given timestapm
def parse_date(timestamp):
    local_tz = pytz.timezone('Asia/Dubai')
    ts = str(timestamp.astimezone(local_tz)).split(' ')
    d = ts[0].split('-')
    date = d[2] + '-' + d[1] + '-' + d[0]
    return date

# Generates a file name with current timestamp
def get_timestamp():
    return str(int(time.time()))

# Returns a dict of all courses with course name as a key and course detail as a value
def get_all_courses(course_object):
    ret = {}
    for i in course_object:
        ret[i.course_name]=i.course_details
    return ret
    
