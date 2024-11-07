from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class UserNet(AbstractUser):
    """ Custom user model
    """
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    ROLE = (
        ('patient', 'patient'),
        ('doctor', 'doctor')
    )
    middleName = models.CharField(max_length=50)
    firstLogin = models.DateTimeField(blank=True, null=True)
    phoneNumber = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    role = models.CharField(max_length=7, choices=ROLE, default='patient')
