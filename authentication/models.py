from django.db import models
from django.contrib.auth.models import User
from .constants import ROLE

# Create your models here.
class AdditionalInfoModel(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture     = models.FileField(upload_to="profile_picture", null=True, blank=True)
    address             = models.CharField(max_length=20)
    role                = models.CharField(max_length=10, choices=ROLE)

    def __str__(self):
        return self.user.username