from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	avatar = models.ImageField(upload_to='images/ser/avatar', null=True, blank=True)


