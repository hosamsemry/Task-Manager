from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register the built-in User model using the built-in UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)