from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserNet


class UserNetAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'email', 'phoneNumber', 'is_staff')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
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
        (_("Additional info"), {"fields": ("phoneNumber", "avatar", "role")}),
    )


admin.site.register(UserNet, UserNetAdmin)

