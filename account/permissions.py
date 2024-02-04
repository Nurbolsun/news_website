from rest_framework import permissions
from django.db.models import Q
from django.contrib.auth.models import Permission


class IsAdminOrReadOnly(permissions.BasePermission): # Только админ могут изменение....
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission): # Только автор могут удалить
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


