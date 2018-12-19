from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
    CustomUser,
    SetupUserProfile,
    Department,
    JobTitle,
    PageAccess,
)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
    ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SetupUserProfile)
admin.site.register(Department)
admin.site.register(JobTitle)
admin.site.register(PageAccess)
