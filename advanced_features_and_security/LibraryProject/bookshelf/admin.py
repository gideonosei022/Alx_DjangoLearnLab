from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add extra fields
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    list_display = ("username", "email", "is_staff", "is_active")

# Explicit registration
admin.site.register(CustomUser, CustomUserAdmin)



