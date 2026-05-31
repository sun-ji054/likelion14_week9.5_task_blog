from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import BlogListSerializer, BlogDetailSerializer, CommentSerializer
from blog.models import Blog, Comment

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
        serializer = BlogListSerializer(blog, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        blog.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommentListAPIView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, id=pk) # id가 pk인 Blog 찾기
        comments = Comment.objects.filter(blog=blog) # 그 Blog의 Comment 필터링(파이썬 객체)
        serializer = CommentSerializer(comments, many = True)
        # serializer: 직렬화. Python 객체 -> Json으로 변환

        return Response(serializer.data)
    
    def post(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(blog=blog) # blog 자동 연결
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
