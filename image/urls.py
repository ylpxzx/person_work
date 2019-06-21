
from django.conf.urls import url
from django.urls import path
from image.views import Image_list,Image_forms,delimages


app_name='image'
urlpatterns = [
    url(r'^image_list/$', Image_list, name='image_list'),
    url(r'^image_form/$', Image_forms, name='image_form'),
    url(r'^delimage/$',delimages,name='delimage'),
]