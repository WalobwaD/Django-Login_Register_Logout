from django.contrib import admin
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'portfolio')
    ordering = ('-id',)
admin.site.register(UserProfile, UserProfileAdmin)