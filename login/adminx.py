from django.contrib import admin
import xadmin
# Register your models here.
from .models import *
# Register your models here.

@xadmin.sites.register(User)
class UserAdmin(object):
    list_display = ('name','sex','email','password','c_time')
    list_filter = ['sex','name','c_time']
    search_fields = ['sex','name','c_time']

@xadmin.sites.register(ConfirmString)
class ConfirmAdmin(object):
    list_display = ('code','user','c_time')



