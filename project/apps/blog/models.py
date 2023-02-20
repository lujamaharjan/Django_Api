
"""
    Domain Class for Blog Applications
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=200)
    proffession = models.CharField(max_length=100)


class Blog(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to="static/images", null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_data = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
