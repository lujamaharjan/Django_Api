from rest_framework import serializers
from .models import Blog, User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ('author',)