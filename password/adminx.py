from django.contrib import admin
import xadmin
from .models import Password
from xadmin.layout import Row,Fieldset
# Register your models here.

@xadmin.sites.register(Password)
class PasswordAdmin(object):
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    form_layout=(
        Fieldset(
            '密码信息',
            'appname',
            Row("user", "password"),
            Row ('email','phone'),
        ),
    )
    list_display = ('appname', 'user', 'email', 'phone', 'password', 'created_time','image_img1')
    list_filter = ['appname', 'created_time']

    def has_delete_permission(self, *args, **kwargs):
        return True
'''
    list_display = ('appname','user','email','phone','password','created_time')
    list_filter = ('appname','created_time')
    search_fields = ('appname','phone','password')
    fieldsets = (
        (None,{
            'fields':(
                'appname',
                ('user', 'password'),
                ('email','phone'),
            )
        }),
    )
admin.site.register(Password,PasswordAdmin)
    '''


