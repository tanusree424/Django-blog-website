from django.contrib import admin
from .models import Contact, UserProfile
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
admin.site.register(Contact)
admin.site.register(UserProfile)
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Specify the fields you want to display in the Django Admin
    list_display = ('username', 'email', 'is_staff', 'is_active', 'role')  # Add more fields as needed
    search_fields = ('username', 'email')
    ordering = ('username',)

    # Define fieldsets to customize the admin panel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional Info', {'fields': ('role',)}),  # If you have a role field
    )