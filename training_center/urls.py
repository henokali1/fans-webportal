from django.urls import path
from . import views


urlpatterns = [
    path('', views.training_center, name='training_center.html'),
    path('admin/', views.admin, name='admin.html'),
    path('enroll_trainee/', views.enroll_trainee, name='enroll_trainee.html'),
    path('trainee/all', views.all_trainees, name='all_trainees.html'),
    path('trainee/<int:pk>/', views.trainee_detail, name='trainee_detail.html'),
    path('trainee/<int:pk>/edit', views.edit_trainee, name='edit_trainee.html'),
]
