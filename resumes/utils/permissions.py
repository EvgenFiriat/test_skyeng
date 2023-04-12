from rest_framework.permissions import BasePermission


class IsAuthorPermission(BasePermission):
    """
    Only resume creator should have the possibility to edit resume
    """
    message = "Access denied"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
