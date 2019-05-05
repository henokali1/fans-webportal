from django.urls import path

from . import views

urlpatterns = [
    path('setup-account/', views.setup_account, name='setup_account.html'),
    path('profile/<str:pk>/', views.profile, name='profile.html'),
]