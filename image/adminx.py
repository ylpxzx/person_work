
import xadmin
from .models import Image
from xadmin.layout import Fieldset
# Register your models here.

@xadmin.sites.register(Image)
class ImageAdmin(object):
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True


    list_display = ('image_img3','created_time')
    list_filter = ['created_time']

    def has_delete_permission(self, *args, **kwargs):
        return True