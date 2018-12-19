from django.urls import path

from . import views

urlpatterns = [
    path('setup-account/', views.setup_account, name='setup_account.html'),
]