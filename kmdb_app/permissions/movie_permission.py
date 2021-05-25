from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAuthenticated
import ipdb

class MoviePermission(BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        verify_super_user = request.user.is_superuser
        verify_staff = request.user.is_staff
        method = request.method
        
        if method == 'GET':
            return True

        if verify_super_user and verify_staff:
            return True
        

