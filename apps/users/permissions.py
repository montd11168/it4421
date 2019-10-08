from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    message = "Action is not allowed"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user or request.user.is_staff
