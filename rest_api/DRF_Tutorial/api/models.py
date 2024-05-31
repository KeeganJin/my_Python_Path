from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    role = models.IntegerField(choices=((1, 'Admin'), (2, 'Manager'), (3, 'Worker')),default=3)

    # can be stored in redis, jwt, ...
    token = models.CharField(max_length=64, null=True)

