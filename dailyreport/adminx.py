
import xadmin
from .models import DailyReport
from xadmin.layout import Fieldset
# Register your models here.

@xadmin.sites.register(DailyReport)
class DailyReportAdmin(object):
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True


    list_display = ('cat_choices','category','content','start_time','end_time','add_time')
    list_filter = ['category']

    def has_delete_permission(self, *args, **kwargs):
        return True