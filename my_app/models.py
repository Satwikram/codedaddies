from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password = None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have a  phone number')

        user = self.model(
            email=self.normalize_userid(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given phone and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.save(using=self._db)
        return user

class Search(models.Model):
    search = models.CharField(max_length = 500)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.search
