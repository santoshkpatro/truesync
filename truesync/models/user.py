from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from . base import BaseUUIDModel


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email=email,
            full_name=full_name,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(BaseUUIDModel, AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    full_name = models.CharField(max_length=100)
    profile = models.CharField(max_length=200, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.email

    @property
    def profile_url(self):
        return 'http//dakhdkjasdada.jpeg'
    

    """Django Admin permission properties and methods"""

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin