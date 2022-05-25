from django.db import models

# Create your models here.
from authentication.models import User 

class Location(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    post = models.TextField(max_length=5000)
    difficulty = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)

class Reply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
