from rest_framework import permissions


class PostUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.Author.id == request.user.id
            print(obj.Author, request.user.id)