# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models


# Create your models here.
class PunishmentModel(models.Model):
    
    no = models.CharField(max_length=50,
                          default=None,
                          unique=True)

    admin_no = models.CharField(max_length=20,
                                default=None,
                                verbose_name=u'录入用户姓名')

    penalty_name = models.CharField(max_length=50,
                                    default=None,
                                    verbose_name=u'被处罚机构名称')

    case_no = models.CharField(max_length=50,
                               blank=True, null=True,
                               verbose_name=u'执行案号')
    
    punished_by = models.CharField(max_length=50,
                                   blank=True, null=True,
                                   verbose_name=u'处罚机构名称')

    company_unified_social_credit_code = models.CharField(max_length=40,
                                                          blank=True, null=True,
                                                          verbose_name=u'统一社会信用代码')
    organization_code = models.CharField(max_length=30,
                                         blank=True, null=True,
                                         verbose_name=u'组织机构代码')
    business_registration_code = models.CharField(max_length=30,
                                                  blank=True, null=True,
                                                  verbose_name=u'工商登记码')
    tax_registration_code = models.CharField(max_length=30,
                                             blank=True, null=True,
                                             verbose_name=u'税务登记码')

    legal_person = models.CharField(max_length=100,
                                    blank=True, null=True,
                                    verbose_name=u'法人')
    penalty_results = models.CharField(max_length=300,
                                       blank=True, null=True,
                                       verbose_name=u'处罚结果')
    case_nature = models.CharField(max_length=100,
                                   blank=True, null=True,
                                   verbose_name=u'案件性质')
    disbelief_level = models.CharField(max_length=30,
                                       blank=True, null=True,
                                       verbose_name=u'失信等级')

    penalty_decision_date = models.CharField(max_length=30,
                                             blank=True, null=True,
                                             verbose_name=u'处罚决定日期')
    source = models.CharField(max_length=100,
                              blank=True, null=True,
                              verbose_name=u'数据来源')
    remark = models.CharField(max_length=100,
                              blank=True, null=True,
                              verbose_name=u'备注')
    image_info = models.CharField(max_length=300,
                                  blank=True, null=True,
                                  verbose_name=u'图片信息')

    country_code = models.CharField(max_length=10,
                                    blank=True, null=True,
                                    verbose_name=u'国家简写')

    punished_basis = models.CharField(max_length=200,
                                      blank=True, null=True,
                                      verbose_name=u'处罚依据')

    punished_reason = models.CharField(max_length=1000,
                                       blank=True, null=True,
                                       verbose_name=u'处罚原因')

    content = models.CharField(max_length=2000,
                               blank=True, null=True,
                               verbose_name=u'原文内容')
    
    created = models.DateTimeField(default=datetime.datetime.now,
                                   verbose_name=u'创建时间')

    modified = models.DateTimeField(auto_now=True,
                                    verbose_name=u'修改时间')

    spider = models.CharField(max_length=20,
                              null=True,
                              blank=True)
    
    class Meta:
        ordering = ('-id', )
        verbose_name = u'处罚信息'
        verbose_name_plural = u'处罚信息'

    def __str__(self):
        return self.penalty_name
