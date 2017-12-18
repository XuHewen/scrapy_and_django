# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


# '用户信息'
class UserProfile(AbstractUser):
    
    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

