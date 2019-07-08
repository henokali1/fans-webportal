from django.contrib import admin
from .models import *

admin.site.site_header = 'SYS Administration'
admin.site.site_title = "Admin Portal"


admin.site.register(EnrollTrainee)
admin.site.register(Course)
admin.site.register(ClassName)
admin.site.register(Subject)
admin.site.register(TraineeAttendance)
admin.site.register(Grade)
admin.site.register(TraineeFeedback)
admin.site.register(CourseMaterial)
