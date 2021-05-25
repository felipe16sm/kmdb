from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAuthenticated
import ipdb

class CreateCommentPermission(BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        verify_super_user = request.user.is_superuser
        verify_staff = request.user.is_staff

        if (not verify_super_user) and (not verify_staff):
            return True

