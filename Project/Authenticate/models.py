from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # portfolio = models.URLField(max_length=200, blank=True)
    # profile_pic = models.ImageField(upload_to='profiles', blank=True)
    
    def __str__(self):
        return self.user.username