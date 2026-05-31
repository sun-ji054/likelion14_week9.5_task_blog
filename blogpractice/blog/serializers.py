from rest_framework import serializers

from accounts.serializers import CustomUserSerializer
from blog.models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField(source = "blog.id", read_only = True)

    class Meta:
        model = Comment
        fields = ["id", "blog_id", "comment", "created_at"]

# - blogs/ 에서의 블로그 글 목록 조회 (GET)
class BlogListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at"]

# 2가지 상황을 커버합니다.
# - blogs/ 에서의 블로그 글 쓰기 (POST)
# - blogs/{int:pk} 에서의 GET, PUT
class BlogDetailSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many = True, read_only = True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at", "comments"]