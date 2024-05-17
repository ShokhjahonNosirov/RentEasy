from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from rest_framework import status
from .serializers import PostSerializer
from .permissions import PostUserOrReadOnly
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
# for swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import render
# Create a common schema view configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# Custom view to handle dynamic URL
def dynamic_swagger_view(request, pk=None):
    return schema_view.with_ui('swagger', cache_timeout=0)(request)

# end swagger

# class HomeView(generics.ListAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

class PostUserOrReadOnly(BasePermission):
    message = 'Editing posts is restricted to the author only.'
    def has_object_permission(self, request, view, obj):
        # print(request.user, "heelo1")
        # print(obj.Author.driver.username, "heelo")
        if request.method in SAFE_METHODS:
            return True
        print(obj.Author.username)
        print(str(request.user))
        return obj.Author.username == str(request.user)


class HomeView(APIView): #PostListView

    def get(self, request, format = None):
        postlar = Post.objects.all()
        serializer = PostSerializer(postlar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Hozirca hamma edit qila oladi.

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):  #, PostUserOrReadOnly):
    #permission_classes = [PostUserOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer