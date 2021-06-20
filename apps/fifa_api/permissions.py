""" Permissions Class """
#Djanfo settings 
from logging import fatal
from config import settings

# Token 
from rest_framework.authtoken.models import Token
# Permissions
from rest_framework import permissions

class IsAuthToken(permissions.BasePermission):
    def has_permission(self, request, view):
        # Revisar si hay token 
        token = settings.TOKEN
        
        if Token.objects.filter(key=token).first():
            return True
        else:
            return False