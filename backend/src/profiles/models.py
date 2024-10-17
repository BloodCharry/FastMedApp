from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """ Custom user model """
    middleName = models.CharField(max_length=50)
    firstLogin = models.DateField(null=True)
    phoneNumber = models.IntegerField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
