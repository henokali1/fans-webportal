from django.urls import path

from . import views

urlpatterns = [
    path('setup-profile/', views.setup_profile, name='setup_profile.html'),
]