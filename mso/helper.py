from users.models import CustomUser, SetupUserAccount
from training_center.models import *
import time
import datetime
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
    
# Returns full name of a given(pk/id) trainee
def get_trainee_name(pk):
    trainee = EnrollTrainee.objects.all().filter(pk=pk)[0]
    return trainee.first_name + ' ' + trainee.last_name

# Returns only unique students from a given attendance record
def get_unique_trainee_ids(records):
    all_student_ids = []
    for i in records:
        if not i.student_id in all_student_ids:
            all_student_ids.append(i.student_id)
    return(all_student_ids)

# Returns total number of classes for a given subject
def get_tot_classes(records):
    given_classes = []
    for i in records:
        if not i.ident in given_classes:
            given_classes.append(i.ident)
    return len(given_classes)

# Returns the total number of classeds attended by a given id number and attendance record
def get_tot_cls_attended(stu_id, records):
    cntr = 0
    for i in records:
        if (i.student_id == stu_id) and (i.attendance_stat == 'present'):
            cntr += 1
    return cntr

# Returns % of total classes attended out of all given classes
def get_per(tca, tcg):
    return int(tca*100.0/tcg)

# Returns formatted ID number(Year + DB PK) of a given student
def get_stud_id(pk):
    trainee = EnrollTrainee.objects.all().filter(pk=pk)[0]
    if int(pk) <= 100:
        id_sq = '0' + str(pk)
    else:
        id_sq = str(pk)

    return str(trainee.enrolled_on)[:4] + id_sq

# Returns attendance status(present, absent....) of a given student pk
def get_att_stat(pk):
    trainee = EnrollTrainee.objects.all().filter(pk=pk)[0]
    return trainee.attendance_stat

# Returns a formated dict with student id, student 
# name and % of atteded classes of a given class and subject
def get_filtered_att(batch, subject_name):
    filtered_att = {}
    records = TraineeAttendance.objects.all().filter(
        attended_class = batch,
        attended_subject = subject_name,
    )
    # Total classes given
    tcg = get_tot_classes(records)

    ids = get_unique_trainee_ids(records)
    for i in ids:
        # Total classes attended
        tca = get_tot_cls_attended(i, records)
        filtered_att[i] = {
            'stud_id': get_stud_id(i),
            'name': get_trainee_name(i),
            'per': get_per(tca, tcg),
        }
    return filtered_att, tcg

# Returns a formated dict with student id, student 
# name and attendance status of atteded classes of a given class and subject
def get_filtered_att_date(batch, subject_name, date):
    filtered_att = {}
    date_sp = date.split('-')
    records = TraineeAttendance.objects.filter(
        att_date__startswith = datetime.date(int(date_sp[2]), int(date_sp[1]), int(date_sp[0])),
        attended_class = batch,
        attended_subject = subject_name,
    )
    
    cnter = 0
    for i in records:
        cnter += 1
        filtered_att[cnter] = {
            'stud_id': get_stud_id(i.student_id),
            'attendance_stat': i.attendance_stat,
            'name': get_trainee_name(i.student_id),
        }

    return(filtered_att)

# Returns a dict of all the student id's and names of a given class and subject
def get_stud_lst(batch, subject_name):
    stud_lst = {}
    students = EnrollTrainee.objects.filter(
        batch=batch,
        approval = 'Accepted',
    )
    cntr = 0
    for i in students:
        cntr += 1
        stud_lst[i.pk] = {
            'stud_id': get_stud_id(i.pk),
            'name': get_trainee_name(i.pk),
        }
    return(stud_lst)

# Returns a dict of all the student id's, names and over all attendance %  of a given class
def get_stud_lst_cls(batch):
    stud_lst = {}
    students = EnrollTrainee.objects.filter(
        course_name=batch,
        approval = 'Accepted',
    )
    
    records = TraineeAttendance.objects.all().filter(
        attended_class = batch,
    )

    # Total classes given
    tcg = get_tot_classes(records)
    ids = get_unique_trainee_ids(records)
    for i in ids:
        # Total classes attended
        tca = get_tot_cls_attended(i, records)
        stud_lst[i] = {
            'stud_id': get_stud_id(i),
            'name': get_trainee_name(i),
            'per': get_per(tca, tcg),
        }
    
    return(stud_lst)

# Returns a dict of all trainees(filtered by class name) with their grades
def get_all_std_grades(batch_name):
    filtered_trainees = {}
    if(len(batch_name) != 0):
        students = EnrollTrainee.objects.filter(
            batch = batch_name,
            approval = 'Accepted',
        )

        for i in students:
            id_num = get_stud_id(i.pk)
            filtered_trainees[id_num] = {
                'pk': i.pk,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'psp_url': i.passport_size_photo.url,
                'grade': get_overall_grade(i.pk, batch_name),
            }
    return filtered_trainees

# Returns a ditc of trainee ID and it's grade(out of 100%) from a given .TXT file
def get_result(raw_data):
    data =  raw_data.split('\n')
    grades = {}
    try:
        for i in data:
            if i != '':
                student_data = i.split(',')
                grades[student_data[2]] = student_data[-1]
    except:
        grades['err']='err'
    return grades

# Returns trainee pk from a given ID number
def get_trainee_pk(id_num):
    if id_num[4] == '0':
        return id_num[5:]
    else:
        return id_num[4:]

# Returns a list of pk of subjects for a given batch
def get_subjects_pk_lst(batch_name):
    batch = ClassName.objects.all().filter(class_name=batch_name)[0]
    course = Course.objects.all().filter(course_name=batch.courses)[0]
    subjects = course.course_subjects_pk
    return eval(subjects)

# Returns Gread of a student for a given batch, subject and trainee pk
def get_trainee_gread(batch_name, subject_name, pk):
    try:
        grades_obj = Grade.objects.all().filter(
            batch = batch_name,
            subject = subject_name,
            trainee_pk = pk
        )[0]
        return grades_obj.value
    except:
        return 0

# Returns grade of all the subjects for a given course and trainee
def get_course_grades(pk, batch_name):
    subjects_pk_list = get_subjects_pk_lst(batch_name)
    subjects = {}
    for i in subjects_pk_list:
        subject_obj = Subject.objects.all().filter(pk=i)[0]
        grade_val = get_trainee_gread(batch_name, subject_obj.subject_name, pk)
        subjects[subject_obj.subject_name] = {
            'grade': grade_val,
            'subject_pk': subject_obj.pk,
            'has_data': (str(grade_val) != '0')
        }
    return subjects

# Returns overall grade(out of 100%) of a given trainee and batch
def get_overall_grade(trainee_pk, batch_name):
    total = 0.0
    course_grades = get_course_grades(trainee_pk, batch_name)
    for i in course_grades:
        total += course_grades[i]['grade']

    num_subjects = len(course_grades)
    avg = round(total/num_subjects, 2)
    return avg
        
# Returns Course Name From a Given Batch Name
def get_course_name(batch_name):
    try:
        batch_obj = ClassName.objects.all().filter(class_name=batch_name)[0]
        return batch_obj.courses
    except:
        return -1

# Returns email addresses of a given batch
def get_email_addresses(batch):
    emails = []
    trainees = EnrollTrainee.objects.all().filter(batch=batch)
    for i in trainees:
        emails.append(i.email)
    return emails
