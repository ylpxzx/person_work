from django.db import models

# Create your models here.


class Contact(models.Model):
    SEX_BOY = 1
    SEX_GIRL = 0
    SEX_ITEMS = (
        (SEX_BOY, '男'),
        (SEX_GIRL, '女'),
    )
    name=models.CharField(max_length=25,verbose_name="姓名")
    relation=models.CharField(max_length=30,verbose_name="关系")
    email=models.EmailField(verbose_name="Email")
    phone=models.CharField(max_length=12,verbose_name="手机号")
    word=models.CharField(max_length=50,verbose_name="职业")
    sex=models.PositiveIntegerField(default=SEX_BOY, choices=SEX_ITEMS, verbose_name="性别")
    created_time=models.DateTimeField(auto_now_add=True,editable=False,verbose_name="创建时间")

    class Meta:
        verbose_name=verbose_name_plural="联系人管理"
        ordering = ['-id']

