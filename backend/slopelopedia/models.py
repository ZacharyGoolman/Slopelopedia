from django.db import models

# Create your models here.
from django.db import models
from authentication.models import User 












class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Reply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)