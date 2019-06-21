from django.db import models
from stdimage.models import StdImageField
# Create your models here.
from DjangoUeditor.models import UEditorField

class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name="名称")

    class Meta:
        verbose_name = verbose_name_plural = '分类'
    def __str__(self):
        return self.name




class Memo(models.Model):
    title=models.TextField(max_length=360,verbose_name='标题',default='生活')
    content=UEditorField(width=600, height=300, toolbars="full", imagePath="images/", filePath="files/",
                         upload_settings={"imageMaxSize":12040000},
                         settings={}, verbose_name='内容')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    image2 = StdImageField(
        upload_to='image/%Y/%m', variations={'thumbnail': {'width': 100, 'height': 75}},
        verbose_name=u"图片",
    )

    class Meta:
        verbose_name = verbose_name_plural = '便签'
        ordering=['-id']

    def image_img2(self):
        if self.image2:
            return str('<img src="%s" />' % self.image2.thumbnail.url)
        else:
            return '上传图片'

    image_img2.short_description = '图片'
    image_img2.allow_tags = True  # 列表页显示图片

