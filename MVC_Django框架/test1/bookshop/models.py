from django.db import models
"""书写与数据库相关的内容
"""


class BookShop(models.Model):
    '''图书类模型'''
    # Charfield 说明是一个字符串，max_length指定字符串最大长度
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()


# Create your models here.
