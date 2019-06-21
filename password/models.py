from django.db import models
from stdimage.models import StdImageField
# Create your models here.
class Password(models.Model):
    appname=models.CharField(max_length=25,verbose_name="备注")
    user=models.CharField(max_length=30,verbose_name="用户名")
    email=models.EmailField(verbose_name="Email")
    phone=models.CharField(max_length=12,verbose_name="手机号")
    password=models.CharField(max_length=50,verbose_name="密码")
    created_time=models.DateTimeField(auto_now_add=True,editable=False,verbose_name="创建时间")
    image1 = StdImageField(
        upload_to='image/%Y/%m', variations={'thumbnail': {'width': 100, 'height': 75}},
        verbose_name=u"图片",
        )

    class Meta:
        verbose_name=verbose_name_plural="密码管理"
        ordering = ['-id']
    def image_img1(self):
        if self.image1:
            return str('<img src="%s" />' % self.image1.thumbnail.url)
        else:
            return '上传图片'

    image_img1.short_description = '图片'
    image_img1.allow_tags = True  # 列表页显示图片