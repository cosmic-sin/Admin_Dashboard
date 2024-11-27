from django.contrib import admin
from .models import CustomUser, Roles, Permission
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Roles)
admin.site.register(Permission)
