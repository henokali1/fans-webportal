from django.urls import path
from . import views


urlpatterns = [
    path('', views.fans_index, name='fans_index.html'),
]