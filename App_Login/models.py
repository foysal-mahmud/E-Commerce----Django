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


    
