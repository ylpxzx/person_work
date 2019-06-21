from django.contrib import admin
import xadmin
from .models import Contact
from xadmin.layout import Row,Fieldset
# Register your models here.

@xadmin.sites.register(Contact)
class ContactAdmin(object):
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    form_layout=(
        Fieldset(
            '联系人信息',
            'word',
            'sex',
            Row("name", "relation"),
            Row ('email','phone'),
        ),
    )
    list_display = ('name', 'relation', 'email', 'phone', 'word', 'created_time','sex')
    list_filter = ['sex', 'created_time','relation']

    def has_delete_permission(self, *args, **kwargs):
        return True

