from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.v1.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    
    list_display = ("id", "username", "email")
    

    def get_fieldsets(self):
        
        fieldsets = super().get_fieldsets()
        return fieldsets
