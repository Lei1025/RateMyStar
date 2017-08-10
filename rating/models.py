from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class IMG(models.Model):
    img = models.ImageField(upload_to='rating/media/upload')

    def __str__(self):
        return self.title


