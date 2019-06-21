from django.conf.urls import url
from django.urls import path
from password.views import Password_list,Password_detail,Password_forms,index,delpasswords


app_name='password'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^password/$', Password_list, name='password'),
    url(r'^password/(?P<password_id>\d+)/$', Password_detail, name="detail_password"),
    url(r'^password_form/$', Password_forms, name='password_form'),
    url(r'^delpassword/$',delpasswords,name='delpassword'),
]