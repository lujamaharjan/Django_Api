
from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .models import Blog
from .serializers import BlogSerializer


class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCreateView(CreateAPIView):
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description='Upload file...',)
    @action(detail=False, methods=['post'])
    def post(self, request, **kwargs):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        blog = Blog(title=data.get('title'), 
            author=request.user, 
            body= data.get('body') ,
            cover_image=data.get('cover_image'))
        blog.save()
        return Response({}, status=status.HTTP_201_CREATED)
        

class BlogDeleteView(DestroyAPIView):
    serializer_class = BlogSerializer

