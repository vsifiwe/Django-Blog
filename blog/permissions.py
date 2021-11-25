from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'Custom permission message.'

    def has_object_permission(self, request, view, obj):
        my_methods = ['GET', 'PUT']

        if request.method in my_methods:
            return True

        return obj.user == request.user
