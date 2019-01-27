from django.urls import path
from . import views


urlpatterns = [
    path('', views.training_center, name='training_center.html'),
    path('admin/', views.admin, name='admin.html'),
    path('trainee/new/', views.enroll_trainee, name='enroll_trainee.html'),
    path('trainee/all/', views.all_trainees, name='all_trainees.html'),
    path('trainee/approve/', views.approve, name='approve.html'),
    path('trainee/approve_application/<int:pk>/', views.approve_application, name='approve.html'),
    path('trainee/reject_application/<int:pk>/', views.reject_application, name='approve.html'),
    path('trainee/<int:pk>/', views.trainee_detail, name='course_enrolment_form_pdf.html'),
    path('trainee/<int:pk>/edit', views.edit_trainee, name='edit_trainee.html'),
]
