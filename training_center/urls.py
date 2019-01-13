from django.urls import path
from . import views


urlpatterns = [
    path('', views.training_center, name='training_center.html'),
    path('admin/', views.admin, name='admin.html'),
    path('enroll_trainee/', views.enroll_trainee, name='enroll_trainee.html'),
]
