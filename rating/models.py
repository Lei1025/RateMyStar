from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from PIL import Image
import datetime
from decimal import Decimal
# Create your models here.
class IMG(models.Model):
    img = models.ImageField(upload_to='rating/media/upload')

    def __str__(self):
        return self.id

class R_User(models.Model):
    username=models.ForeignKey(settings.AUTH_USER_MODEL)
    profile_picture=models.ImageField(upload_to='rating/media/profile')
    def __str__(self):
        return self.username

class Article(models.Model):
    CATEGORY_CHOICES=(
        ('Musicians','Musicians'),
        ('Authors','Authors'),
        ('Actors','Actors'),
        ('Athletes','Athlets'),
        ('Hosts','Hosts')
    )
    #id = models.AutoField(primary_key=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,default='Username')
    date=models.DateField(default=datetime.date.today)
    title=models.CharField(max_length=100)
    age=models.PositiveIntegerField(default=0)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    nationality=models.CharField(max_length=100)
    thumbnail=models.ImageField(upload_to='rating/media/article/thumbnail',default="Please uplaod a thumbnail picture.")
    banner=models.ImageField(upload_to='rating/media/article/banner',default="Please upload a banner picture.")
    content=models.TextField(max_length=10000)

    def __str__(self):
        return self.title

class Score(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default='username')
    title=models.ForeignKey(Article)
    C1=models.DecimalField(decimal_places=1,max_digits=2,default=Decimal(0.0))
    C2=models.DecimalField(decimal_places=1,max_digits=2,default=Decimal(0.0))
    C3 = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    C4 = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    C5 = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    def __str__(self):
        return self.title