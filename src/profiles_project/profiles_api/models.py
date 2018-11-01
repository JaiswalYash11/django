# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class userProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object"""
        if not email:
            raise ValueError('Users must have a n email address.')

        email=self.normalize_email(email)
        user= self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_super_user (self, name ,email, password):
        """Creates and saves a new superuser with given details"""

        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a 'user profile' inside our system."""
    email = models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active =models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    objects= userProfileManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS =['name']

    """Used to get a users full name"""
    def get_full_name(self):
        return self.name

    """Used to get a users full name"""
    def get_short_name(self):
        return self.name

    """DJANGO uses this when it needs to convert the object to a string"""
    def __str__(self):
        return self.email
