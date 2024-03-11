from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class HomeView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()