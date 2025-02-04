from django.contrib.auth.models import AbstractUser
from django.db import models


from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):
    # Add custom fields to the user model
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email=models.EmailField(max_length=30,unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth =models.DateField(blank=True, null=True)
    gender =models.CharField(max_length=10)
    Bank_Account = models.CharField(max_length=20)

    objects = CustomUserManager()

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'  # Set email as the unique identifier for login
    REQUIRED_FIELDS = ['username']  # Specify required fields


    def __str__(self):
        return self.email
