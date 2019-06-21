
from django.conf.urls import url
from django.urls import path
from contact.views import Contact_list,delcontacts,Contact_forms


app_name='contact'
urlpatterns = [
    url(r'^contact_list/$', Contact_list, name='contact_list'),
    #url(r'^memo_list/(?P<memo_id>\d+)/$', Memo_detail, name="detail_memo"),
    url(r'^contact_form/$', Contact_forms, name='contact_form'),
    url(r'^delcontact/$',delcontacts,name='delcontact'),
]