# -*- coding:utf-8 -*-
from django.contrib import admin

import xadmin
from utils import md5
from xadmin import views

from .forms import LeaderProfileForm
from .models import LeaderProfile

from django.contrib import messages


# xadmin 全局配置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'TransferEasy'
    site_footer = 'TransferEasy'
    # menu_style = 'accordion'

    # def get_site_menu(self):
    #     return ({'title': u'领导人信息管理',
    #              'perm': self.get_model_perm(LeaderProfile, 'change')}, )


class LeaderProfileAdmin(object):
    form = LeaderProfileForm

    list_display = ['id', 'admin_no', 'name']
    search_fields = ['admin_no', 'name']
    list_filter = ['admin_no']
    list_per_page = 20
    list_max_show_all = 100

    # exclude = ('birth', )

    # fields = ('name', 'gender', 'ethnicity',
    #           'birth_of_year', 'birth_of_month', 'birth_of_day',
    #           'position', 'purposed_position', 'place_of_birth',
    #           'photo_img', 'source', 'status', 'review_notes', 'remark')

    fields = ('name', 'position', 'source', 'remark', 'gender', 'ethnicity',
              'birth_of_year', 'birth_of_month', 'birth_of_day',
              'purposed_position', 'place_of_birth',
              'photo_img', 'status', 'review_notes')

    def queryset(self):
        qs = LeaderProfile.objects
        if self.request.user.is_superuser:
            return qs.all()
        return qs.filter(admin_no=self.request.user.username)

    def save_models(self):
        obj = self.new_obj
        request = self.request
        
        year = request.POST.get('birth_of_year')
        month = request.POST.get('birth_of_month')
        day = request.POST.get('birth_of_day')

        obj.admin_no = request.user.username

        if not year:
            year = u'*'

        if not month:
            month = u'*'

        if not day:
            day = u'*'

        if year != u'*' or month != u'*' or day != u'*':

            obj.birth = year + '-' + month + '-' + day

        md5_string = year + month + day + request.POST.get('name') + request.POST.get('gender') + request.POST.get('source')
        obj.no = md5(md5_string)
        
        try:
            obj.save()
            # messages.add_message(request, messages.INFO, u'保存成功')
        except:
            # messages.add_message(request, messages.INFO, u'保存失败')
            pass


xadmin.site.register(LeaderProfile, LeaderProfileAdmin)

# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
