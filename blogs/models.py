from django.db import models
from django.contrib.auth.models import User
from .constants import CATEGORY

# Create your models here.
class blogsModel(models.Model):
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    img         = models.URLField(max_length=800)
    category    = models.CharField(choices=CATEGORY, max_length=50)
    summary     = models.TextField()
    content     = models.CharField(max_length=50)
    draft       = models.BooleanField(default=False)

    def __str__(self):
        return self.title
