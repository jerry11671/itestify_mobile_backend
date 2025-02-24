from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, Group, Permission
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timezone
from django.conf import settings

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    groups = models.ManyToManyField(Group, related_name="customuser_groups")  
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions") 
    
    objects = CustomUserManager()
    USERNAME_FIELDS = ['email']
    REQUIRED_FIELDS = ['full_name']


    def token(self):
        refresh = RefreshToken.for_user(self)
        tokens =  {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
        return tokens
    
    
class Otp(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def check_expiration(self):
        now = timezone.now()
        diff = now - self.updated_at

        if diff.total_seconds() > settings.EMAIL_OTP_EXPIRE_SECONDS:
            return True
        return False 

