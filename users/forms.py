from django.contrib.auth.models import User
from .models import UserProfile
# Profile

from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

# class UpdateProfileForm(forms.ModelForm):
   
    
#     class Meta:
#         model: Profile
#         fields = ['profile_pic', 'bio']

# class UpdateUserForm(forms.ModelForm):
    

#     class Meta:
#         model = User
#         fields = ['username', 'email']