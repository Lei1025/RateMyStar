from django.conf import settings
from django.contrib.auth.models import User,UserManager
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
    user=models.OneToOneField(User,default='new user',related_name='profile')
    profile=models.ImageField(upload_to='profile',default='profile/user.png')

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)

class Article(models.Model):
    CATEGORY_CHOICES=(
        ('Musicians','Musicians'),
        ('Authors','Authors'),
        ('Actors','Actors'),
        ('Athletes','Athletes'),
        ('Models', 'Models'),
        ('Hosts','Hosts'),
    )
    #id = models.AutoField(primary_key=True)
    author=models.ForeignKey(User,default='Username')
    date=models.DateField(default=datetime.date.today)
    title=models.CharField(max_length=100)
    age=models.PositiveIntegerField(default=0)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    nationality=models.CharField(max_length=100)
    thumbnail=models.ImageField(upload_to='article/thumbnail',default="Please uplaod a thumbnail picture.")
    banner=models.ImageField(upload_to='article/banner',default="Please upload a banner picture.")
    users= models.PositiveIntegerField(default=0)
    C1 = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    C2 = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    C3 = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    C4 = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    C5 = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    AVG = models.DecimalField(decimal_places=1, max_digits=2, default=Decimal(0.0))
    content=models.TextField(max_length=10000)


    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(R_User)
    article=models.ForeignKey(Article)
    time=models.DateTimeField()
    text=models.TextField(max_length=500)
    def __str__(self):
        return str(self.user) +' posted in '+str(self.article)

