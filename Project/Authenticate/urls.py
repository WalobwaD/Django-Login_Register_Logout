from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('success/', special, name="success"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
