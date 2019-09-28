from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django_countries.fields import CountryField


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Creates and saves a new super user"""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=255)
    domain_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'users'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    country = CountryField()
