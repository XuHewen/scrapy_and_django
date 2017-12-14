from django.contrib.auth.models import AbstractUser
from django.db import models


# user model
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,
                                 verbose_name='昵称', default='Hello')
    gender = models.CharField(max_length=5,
                              choices=(('male', '男'), ('female', '女')),
                              default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/user/%Y/%m',
                              default='image/user/default.png',
                              max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
