
import json
import pytest
from django.urls import reverse
from django.test import Client
from rest_framework import status
from rest_framework.test import APIClient
from apps.blog.models import Blog
from apps.blog.serializers import BlogSerializer
from apps.blog.models import User

@pytest.mark.django_db
def test_blog_create():
    # Create a test client and request the blog list view
    user = User.objects.create_user(username="luja", email="sachin@gmail.com", password="password")
    user.save()
    client1 = APIClient()
    res = client1.post(reverse('token_obtain_pair'), {'username': 'luja', 'password':'password'}).content.decode()
    token = json.loads(res).get('access')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.post(reverse('blog_create'), data = {'title': 'Test Blog 1', 'body' : 'body1'})

    # Check that the response contains the expected data
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_blog_list():
    user = User.objects.create_user(username="luja", email="sachin@gmail.com", password="password")
    user.save()

    Blog.objects.create(title='Test Blog 1', body="hello world", author=user)
    Blog.objects.create(title='Test Blog 2', body="hello world", author=user)
    
    client = APIClient()
    response = client.get(reverse('blog_list'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert 'Test Blog 2' in response.content.decode()


@pytest.mark.django_db
def test_blog_detail():
    user = User.objects.create_user(username="luja", email="sachin@gmail.com", password="password")
    user.save()

    Blog.objects.create(title='Test Blog 1', body="hello world", author=user)
    Blog.objects.create(title='Test Blog 2', body="hello world", author=user)
    
    client = APIClient()
    response = client.get(reverse('blog_detail', args=[1]))

    assert response.status_code == status.HTTP_200_OK
    assert 'Test Blog 1' in response.content.decode()
    assert 'Test Blog 2' not in response.content.decode()



