
from django.conf.urls import url
from django.urls import path
from memo.views import Memo_list,Memo_detail,Memo_forms,delmemos


app_name='memo'
urlpatterns = [
    url(r'^memo_list/$', Memo_list, name='memo_list'),
    url(r'^memo_list/(?P<memo_id>\d+)/$', Memo_detail, name="detail_memo"),
    url(r'^memo_form/$', Memo_forms, name='memo_form'),
    url(r'^delmemo/$',delmemos,name='delmemo'),
]