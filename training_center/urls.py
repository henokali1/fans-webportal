from django.urls import path
from . import views


urlpatterns = [
    path('', views.training_center, name='training_center.html'),
    path('admin/', views.admin, name='admin.html'),
    path('attendance/', views.trainer, name='attendance.html'),
    path('take_attendance/<str:batch>/<str:subject_name>/', views.take_attendance, name='take_attendance.html'),
    path('trainee/new/', views.enroll_trainee, name='enroll_trainee.html'),
    path('trainees/all/', views.all_trainees, name='all_trainees.html'),
    path('trainee/approve/', views.approve, name='approve.html'),
    path('trainee/approve_application/<int:pk>/<str:batch>/', views.approve_application, name='approve.html'),
    path('trainee/reject_application/<int:pk>/', views.reject_application, name='approve.html'),
    path('trainee/<int:pk>/', views.trainee_detail, name='course_enrolment_form_pdf.html'),
    path('trainee/<int:pk>/edit', views.edit_trainee, name='edit_trainee.html'),
    path('create_class/', views.create_class, name='create_class.html'),
    path('all_classes/', views.all_classes, name='classes.html'),
    path('class/<int:pk>/edit/', views.edit_class, name='edit_class.html'),
    path('subjects/new/', views.create_subject, name='create_subject.html'),
    path('subjects/all/', views.all_subjects, name='all_subjects.html'),
    path('subjects/<int:pk>/edit/', views.edit_subject, name='edit_subject.html'),
    path('courses/new/', views.create_course, name='create_course.html'),
    path('courses/all/', views.all_courses, name='all_courses.html'),
    path('courses/<int:pk>/edit/', views.edit_course, name='edit_course.html'),
    path('view_subject_attendance/<str:class_name>/<str:subject_name>/', views.view_subject_attendance, name='view_subject_attendance.html.html'),
    path('view_attendance_subj_date/<str:class_name>/<str:subject_name>/<str:date>/', views.view_attendance_subj_date, name='view_attendance_subj_date.html'),
    path('view_attendance_cls/<str:class_name>/', views.view_attendance_cls, name='view_attendance_cls.html'),
    path('dashboard/', views.dashboard, name='dashboard.html'),
    path('grades/', views.grades, name='grades.html'),
    path('grades/all/<str:batch_name>/', views.all_grades, name='all_grades.html'),
    path('icons/', views.icons, name='icons.html'),
]
