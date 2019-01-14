from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('user/', include('users.urls')),
    path('mso/', include('mso.urls')),
    path('logbook/', include('logbook.urls')),
    path('cns_monthly_check/', include('cns_monthly_check.urls')),
    path('training_center/', include('training_center.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)