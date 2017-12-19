# -*- coding:utf-8 -*-
from django.db import models
import datetime


class LeaderManager(models.Manager):
    def get_queryset(self):

        return super(LeaderManager, self).get_queryset()


# Create your models here.
class LeaderProfile(models.Model):
    objects = LeaderManager()

    GENDER_CHOICE = (
        ('male', u'男'),
        ('female', u'女'),
    )
    YEAR_CHOICES = []
    MONTH_CHOICES = []
    for r in range(1930, (datetime.datetime.now().year - 18)):
        YEAR_CHOICES.append((r, r))
    for m in range(12):
        if m < 9:
            m = '0' + str(m+1)
            MONTH_CHOICES.append((m, m))
        else:
            MONTH_CHOICES.append((m+1, m+1))

    name = models.CharField(max_length=40,
                            verbose_name=u'姓名')
    gender = models.CharField(max_length=7,
                              choices=GENDER_CHOICE,
                              null=True,
                              blank=True,
                              verbose_name=u'性别')
    ethnicity = models.CharField(max_length=10,
                                 null=True,
                                 blank=True,
                                 default=u'汉族',
                                 verbose_name=u'民族')

    # year_of_birth = models.CharField(max_length=4,
    #                                 #  choices=YEAR_CHOICES,
    #                                  null=True,
    #                                  blank=True,
    #                                  verbose_name=u'出生年份')

    # month_of_birth = models.CharField(max_length=2,
    #                                 #   choices=MONTH_CHOICES,
    #                                   null=True,
    #                                   blank=True,
    #                                   verbose_name=u'出生月份')

    # day_of_birth = models.CharField(max_length=4,
    #                                 null=True,
    #                                 blank=True,
    #                                 verbose_name=u'出生日')

    birth = models.CharField(max_length=15,
                             null=True,
                             blank=True,
                             help_text=u'格式: 1999-01-01 (没有用*代替)',
                             verbose_name=u'生日')
    
    position = models.CharField(max_length=40,
                                default=None,
                                verbose_name=u'现任职位')

    purposed_position = models.CharField(max_length=40,
                                         default=None,
                                         blank=True,
                                         null=True,
                                         verbose_name=u'拟任职位')
    
    place_of_birth = models.CharField(max_length=40,
                                      null=True,
                                      blank=True,
                                      verbose_name=u'出生地')
    photo_img = models.URLField(null=True,
                                blank=True,
                                verbose_name=u'图片链接')
    remark = models.TextField(verbose_name=u'备注',
                              default=None)

    class Meta:
        ordering = ('-id', )
        verbose_name = u'领导人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
