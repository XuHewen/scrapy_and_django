import xadmin
from utils import md5

from .forms import PunishmentForm
from .models import PunishmentModel


class PunishmentAdmin(object):
    
    list_display = ['id', 'admin_no', 'penalty_name']
    search_fields = ['penalty_name', 'admin_no']
    list_filter = ['admin_no']
    list_per_page = 20
    list_max_show_all = 100
    
    form = PunishmentForm

    exclude = ('admin_no', 'no', 'created', 'modified', 'spider')

    def save_models(self):
        obj = self.new_obj
        request = self.request

        obj.admin_no = request.user.username

        md5_string = request.POST.get('penalty_name') +\
                     request.POST.get('source') +\
                     request.POST.get('case_no') +\
                     request.POST.get('punished_by')

        obj.no = md5(md5_string)

        obj.save()

xadmin.site.register(PunishmentModel, PunishmentAdmin)
