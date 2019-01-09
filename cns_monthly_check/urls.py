from django.urls import path
from . import views


urlpatterns = [
    path('', views.cns_monthly_check, name='cns_monthly_check.html'),
    path('vhf_ground_to_air_radios/', views.vhf_ground_to_air_radios, name='vhf_ground_to_air_radios.html'),
]
