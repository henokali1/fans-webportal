from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.new_log, name='new_logbook.html'),
    path('all/', views.all_logs, name='all_logs.html'),
]
