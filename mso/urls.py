from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_msos, name='all_msos.html'),
    path('approve/', views.approve, name='approve.html'),
]