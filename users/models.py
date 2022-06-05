from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class UserProfile(models.Model):
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username





# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pic', blank=True)

#     bio = models.TextField()
    

#     def __str__(self):
#         return self.user.username

#     # resizing images
#     def save(self, *args, **kwargs):
#         super().save()

#         img = Image.open(self.profile_pic.path)

#         if img.height > 100 or img.width > 100:
#             new_img = (100, 100)
#             img.thumbnail(new_img)
#             img.save(self.profile_pic.path)
