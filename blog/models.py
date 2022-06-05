from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_img', blank=True)



    FRONTEND = 'Frontend'
    BACKEND = 'Backend'
    FULLSTACK = 'Fullstack'

    CATEGORY = [
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
        (FULLSTACK, 'Fullstack'),
    ]

    category = models.CharField( max_length=50, choices=CATEGORY, default=FRONTEND)

    DRAFT = 'Draft'
    PUBLISHED  = 'Published'

    STATUS = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    status = models.CharField(max_length=50, choices=STATUS, default=DRAFT)

    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    content = models.TextField()

    def __str__(self):
        return self.content

  

