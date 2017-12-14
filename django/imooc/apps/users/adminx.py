import xadmin

from .models import EmailVerifyRecord, Banner
from xadmin import views


# xadmin 全局配置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'imooc'
    site_footer = 'xuhewen'
    menu_style = 'accordion'

    
# 注册 user model
class EmailVerifyRecordAdmin(object):
    # 显示列  
    list_display = ['id', 'code', 'email', 'send_type', 'send_time']
    # 搜索
    search_fields = ['code', 'email', 'send_type']
    # 筛选
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
