from django.db import models

# Create your models here.

class Department(models.Model):
    """Department Table"""
    title = models.CharField(verbose_name="Department Title", max_length=32)

class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    account = models.DecimalField(max_digits=18,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="enroll time")

    # Django中的约束
    gender_choices = (
        (1, "male"),
        (0, "female"),
    )
    gender = models.SmallIntegerField(verbose_name="gender",choices=gender_choices)

    depart = models.ForeignKey(to="Department", to_field="id",on_delete=models.CASCADE)

