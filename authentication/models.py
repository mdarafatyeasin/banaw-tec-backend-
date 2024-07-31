from django.db import models
from django.contrib.auth.models import User
from .constants import ROLE

# Create your models here.
class AdditionalInfoModel(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture     = models.URLField(max_length=800)
    address             = models.CharField(max_length=100)
    role                = models.CharField(max_length=10, choices=ROLE)

    def __str__(self):
        return self.user.username