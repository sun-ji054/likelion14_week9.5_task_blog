from rest_framework import serializers
from blog.models import Blog, Comment
# from accounts.serializers import CustomUserSerializer

class CommentSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField(source = "blog.id", read_only = True)
    # blog_id: 응답에서 보여줄 이름, source: 데이터 어디서 가져올지 경로
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "blog_id", "comment", "created_at"]

# - blogs/ 에서의 블로그 글 목록 조회 (GET)
class BlogListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at"]

# 2가지 상황을 커버합니다.
# - blogs/ 에서의 블로그 글 쓰기 (POST)
# - blogs/{int:pk} 에서의 GET, PUT
class BlogDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at", "comments"]