from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserNet, Patient, Doctor


class UserNetAdmin(BaseUserAdmin):
    list_display = ('username', 'email',)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified', 'first_name', 'last_name', 'role')
    list_editable = ['verified']
    fieldsets = (
        (None, {"fields": ("user",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "phone", "avatar", "gender", "birthday", "role")}),
        (_("Permissions"), {"fields": ("verified",)}),
    )


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'education', 'certification', 'experience')
    fieldsets = (
        (None, {"fields": ("user",)}),
        (_("Professional info"), {"fields": ("specialization", "education", "certification", "bio", "experience")}),
    )


admin.site.register(UserNet, UserNetAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
