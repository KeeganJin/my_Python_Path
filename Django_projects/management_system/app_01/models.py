from django.db import models
from django.forms import ModelForm
# Create your models here.


class Admin(models.Model):
    username = models.CharField(verbose_name="Username", max_length=32)
    password = models.CharField(verbose_name="Password", max_length=64)
class Department(models.Model):
    title = models.CharField(verbose_name='Title',max_length=32)
    # Object oriented part
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name = models.CharField(verbose_name='Name',max_length=32)
    password = models.CharField(verbose_name='Password',max_length=64)
    age = models.IntegerField(verbose_name='Age')
    account = models.DecimalField(verbose_name='Account',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name='start_time')

    # with constraints,
    # to indicate which table,
    department = models.ForeignKey(to='Department', to_field='id',on_delete=models.CASCADE)

    gender_choices = (
        (0,"female"),
        (1,"male"),
    )
    gender = models.SmallIntegerField(verbose_name='gender', choices=gender_choices)

class FancyNum(models.Model):
    " Fancy Number Table"
    mobile = models.CharField(verbose_name='Mobile Number',max_length=11)
    price = models.IntegerField(verbose_name='Price')
    level_choices = (
        (1,"basic"),
        (2,"premium"),
        (3,"vip"),
    )
    level = models.SmallIntegerField(verbose_name='level', choices=level_choices,default=1)

    status_choices = (
        (0,"taken"),
        (1,"free"),
    )
    status = models.SmallIntegerField(verbose_name='status', choices=status_choices,default=1)







