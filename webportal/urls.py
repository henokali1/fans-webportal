from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('user/', include('users.urls')),
    path('mso/', include('mso.urls')),
    path('logbook/', include('logbook.urls')),
]
