from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    USER_CHOICES = (
        ('admin', 'admin'),
        ('edit', 'edit'),
        ('view', 'view'),
    )

    email = models.EmailField('email', unique=True)
    usertype = models.CharField(max_length=20, choices=USER_CHOICES, default='view')
    image = models.ImageField(upload_to='media', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('created_at',)

    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')