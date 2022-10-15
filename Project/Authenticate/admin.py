from django.contrib import admin
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    ordering = ('-id',)
admin.site.register(UserProfile, UserProfileAdmin)
