from django.contrib import admin
import xadmin
from .models import Memo,Category
from xadmin.layout import Fieldset
# Register your models here.

@xadmin.sites.register(Memo)
class MemoAdmin(object):
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True
    style_fields = {"content": "ueditor"}
    form_layout=(
        Fieldset(
            '便签',
            'title',
            'content',
            'category',
        ),
    )
    list_display = ('title','content', 'category','image_img2','created_time')
    list_filter = ['title','category', 'created_time']
    def has_delete_permission(self, *args, **kwargs):
        return True

@xadmin.sites.register(Category)
class CategoryAdmin(object):


    form_layout = (
        Fieldset(
            '分类',
            'name',
        ),
    )

    #list_display是元组形式的，如果是list_display=('name')，少个逗号，他获取的是’n‘这个字母，而不是'name'
    list_display=('name',)



    def has_delete_permission(self, *args, **kwargs):
        return True
