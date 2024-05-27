from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.v1.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    
    list_display = ("id", "username", "email")
    

    def get_fieldsets(self, request, obj = None):
        
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets = (
            (None, {"fields": ("email", "username", "password")}),
            ("Personal info", {"fields": ("first_name", "last_name")})
        ) + fieldsets[2:]

        return fieldsets
