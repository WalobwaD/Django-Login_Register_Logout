from django import forms
from django.contrib.auth.models import User 
from .models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget= forms.PasswordInput(attrs={
        'class':'form-control',
    }))
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username' : None
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder':'username',
                'class': 'username form-control'}),
            'email': forms.TextInput(attrs={
                'placeholder':'email',
                'class': 'email form-control'}),
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfolio', 'profile_pic')
        widgets = {
            'portfolio': forms.TextInput(attrs={
                'class': 'portfolio form-control',
                'placeholder': 'portfolio link'}),
            'profile_pic' : forms.TextInput(attrs={
                'class': 'profile_pic form-control',
                'placeholder': 'profile photo'}),
        }