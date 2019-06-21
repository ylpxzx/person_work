"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from project.settings import MEDIA_ROOT
import xadmin
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from dailyreport import views
from login import views as view
urlpatterns = [
    path('',include('contact.urls')),
    path('',include('image.urls')),
    path('',include('password.urls')),
    path('',include('memo.urls'),),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^xadmin/', xadmin.site.urls, name='xadmin'),
    url(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('admin/', admin.site.urls),

    url(r'^login/', view.login),
    url(r'^register/', view.register),
    url(r'^logout/', view.logout),
    url(r'^captcha', include('captcha.urls')),
    url(r'^confirm/$', view.user_confirm),

    url(r'^myreport/$', views.MyReportView.as_view(), name='myreport'),
    url(r'^myreport/create$', views.ReportCreateView.as_view(), name='myreport-create'),
    url(r'^myreport/detail$', views.ReportDetailView.as_view(), name='myreport-detail'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

