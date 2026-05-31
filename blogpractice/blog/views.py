from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import BlogListSerializer, BlogDetailSerializer
from blog.models import Blog

# 클래스형 뷰
class BlogListAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = BlogListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailAPIView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = BlogDetailSerializer(blog)

        return Response(serializer.data)

    def patch(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = BlogDetailSerializer(blog, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        blog.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)