# -*- coding:utf-8 -*-
from django.db import models
import datetime


# class LeaderManager(models.Manager):
#     def queryset(self):
#         return super(LeaderManager, self).get_queryset()


# Create your models here.
class LeaderProfile(models.Model):
    # objects = LeaderManager()

    GENDER_CHOICE = (
        ('male', u'男'),
        ('female', u'女'),
    )

    no = models.CharField(max_length=50, default=None, unique=True)

    admin_no = models.CharField(max_length=50,
                                default=None,
                                verbose_name=u'录入用户姓名')

    name = models.CharField(max_length=50,
                            verbose_name=u'姓名')

    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICE,
                              null=True,
                              blank=True,
                              verbose_name=u'性别')

    ethnicity = models.CharField(max_length=20,
                                 null=True,
                                 blank=True,
                                 verbose_name=u'民族')

    birth = models.CharField(max_length=30,
                             null=True,
                             blank=True,
                             help_text=u'格式: 1999-01-01 (没有用*代替)',
                             verbose_name=u'生日')
    
    position = models.CharField(max_length=500,
                                null=True,
                                blank=True,
                                verbose_name=u'现任职位')

    purposed_position = models.CharField(max_length=500,
                                         blank=True,
                                         null=True,
                                         verbose_name=u'拟任职位')
    
    place_of_birth = models.CharField(max_length=50,
                                      null=True,
                                      blank=True,
                                      verbose_name=u'出生地')
    
    photo_img = models.CharField(max_length=500,
                                 null=True,
                                 blank=True,
                                 verbose_name=u'图片链接')

    source = models.CharField(max_length=500,
                              null=True,
                              blank=True,
                              verbose_name=u'原文地址')
    
    review_notes = models.CharField(max_length=50,
                                    null=True,
                                    blank=True,
                                    verbose_name=u'审核备注')

    status = models.CharField(max_length=20,
                              null=True,
                              blank=True,
                              verbose_name=u'状态')

    remark = models.CharField(max_length=1000,
                              null=True, blank=True,
                              verbose_name=u'原文')

    created = models.DateTimeField(default=datetime.datetime.now,
                                   verbose_name=u'创建时间')

    modified = models.DateTimeField(auto_now=True,
                                    verbose_name=u'修改时间')

    spider = models.CharField(max_length=20,
                              null=True,
                              blank=True)

    class Meta:
        ordering = ('-id', )
        verbose_name = u'领导人信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
