from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_msos, name='all_msos.html'),
    path('approve/', views.approve, name='approve.html'),
    path('new/', views.new_mso, name="new_mso.html"),
    path('all/', views.all_msos, name="all_msos.html"),
    path('my/', views.my_msos, name="my_msos.html"),
    path('<int:pk>/', views.mso_preview, name='mso_preview.html'),
    path('edit/<int:pk>/', views.edit_mso, name='edit_mso.html'),
    path('delete/<int:pk>/', views.delete_mso),
    path('approve_mso/<int:pk>/<str:job_title>/', views.approve_mso),
    path('dashboard/', views.dashboard, name="dashboard.html"),
]
