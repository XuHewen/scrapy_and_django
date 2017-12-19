# -*- coding:utf-8 -*-
import xadmin
from xadmin import views

from .models import LeaderProfile
from django.contrib import admin
from .forms import LeaderProfileForm


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

    form = LeaderProfileForm

    exclude = ('birth', )

    fields = ('name', 'gender', 'ethnicity',
              'birth_of_year', 'birth_of_month', 'birth_of_day',
              'position', 'purposed_position', 'place_of_birth',
              'photo_img', 'remark')

    def save_models(self):
        obj = self.new_obj
        request = self.request
        
        year = request.POST.get('birth_of_year')
        month = request.POST.get('birth_of_month')
        day = request.POST.get('birth_of_day')

        if not year:
            year = u'*'

        if not month:
            month = u'*'

        if not day:
            day = u'*'

        if year != u'*' or month != u'*' or day != u'*':

            obj.birth = year + '-' + month + '-' + day
        obj.save()


xadmin.site.register(LeaderProfile, LeaderProfileAdmin)

# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)