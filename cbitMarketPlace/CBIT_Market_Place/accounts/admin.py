from django.contrib import admin
from django.contrib import admin
from accounts.models import UserProfile
# Register your models here.
admin.site.register(UserProfile)


class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','user_info')
