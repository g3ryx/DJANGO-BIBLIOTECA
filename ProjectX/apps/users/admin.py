from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import hashlib
from .models import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'nombre', 'apellido', 'usertype', 'created_at', 'image', 'is_active')
    list_filter = ('usertype',)
    fieldsets = (
        (None, {'fields': ('email', 'usertype', 'image', 'nombre', 'apellido', 'password',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'usertype', 'image', 'nombre', 'apellido', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
