from django.db import models
from stdimage.models import StdImageField
# Create your models here.
class Image(models.Model):
    created_time=models.DateTimeField(auto_now_add=True,editable=False,verbose_name="创建时间")
    image3 = StdImageField(
        upload_to='image/%Y/%m', variations={'thumbnail': {'width': 100, 'height': 75}},
        verbose_name=u"图片",
        )

    class Meta:
        verbose_name=verbose_name_plural="照片管理"
        ordering = ['-id']
    def image_img3(self):
        if self.image3:
            return str('<img src="%s" />' % self.image3.thumbnail.url)
        else:
            return '上传图片'

    image_img3.short_description = '图片'
    image_img3.allow_tags = True  # 列表页显示图片