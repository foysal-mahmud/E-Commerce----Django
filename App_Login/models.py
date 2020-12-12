from django.db import models

# To create a Custom User Model and Admin panel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy

# Create your models here.
class MyUserManager(BaseUserManager):
    """ A Custom Manager to deal with emails as unique identifier """
    def _create_user(self, email, password, **extra_fields):         # username optional thakbe.. email and password diye e kaj hobe.
        """ Creates and saves a user with email and password """

        if not email:
            raise ValueError("The Email must be Required!!!")

        email = self.normalize_email(email)   # exactly jemon ase temon likte hobe
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    # Create Super user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
