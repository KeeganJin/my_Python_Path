import random
from  rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 3:
            return True
        return False

class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role ==2:
            return True
        return False

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role ==1:
            return True
        return False