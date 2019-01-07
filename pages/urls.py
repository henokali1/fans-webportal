from django.urls import path
from . import views


urlpatterns = [
    path('', views.fans_index, name='fans_index.html'),
    path('who_we_are', views.who_we_are, name='who_we_are.html'),
    path('training_center', views.training_center, name='training_center.html'),
    path('services_ats', views.services_ats, name='services_ats.html'),
    path('services_engineering', views.services_engineering, name='services_engineering.html'),
    path('photo_gallery', views.photo_gallery, name='photo_gallery.html'),
]