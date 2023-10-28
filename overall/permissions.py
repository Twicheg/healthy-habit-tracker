from rest_framework.permissions import BasePermission


class OwnerPermission(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.is_superuser:
            return True

        if request.user.id == view.get_object().owner.id:
            return True
