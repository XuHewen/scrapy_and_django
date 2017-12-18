# -*- coding:utf-8 -*-
import xadmin
from xadmin import views

from .models import LeaderProfile
from django.contrib import admin


# xadmin 全局配置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'TransferEasy'
    site_footer = 'TransferEasy'
    # menu_style = 'accordion'


class LeaderProfileAdmin(object):
    list_display = ['id', 'name', 'gender', 'position']
    search_fields = ['name']
    # list_filter = ['name']
    list_per_page = 20
    list_max_show_all = 100

    # def get_queryset(self, request):
    #     qs = super(LeaderProfileAdmin, self).get_queryset(request)
    #     return qs.filter(name='aD')


xadmin.site.register(LeaderProfile, LeaderProfileAdmin)

# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
