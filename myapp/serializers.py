from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='ca   tegory.name')

    class Meta:
        model = Post
        fields = '__all__'
            # ['name', 'course_image', 'about']