from django.db import models

# Create your models here.
class BookInfo(models.Model):
    '''图书表模型'''
    # 图书名称
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDeslete = models.BooleanField(default=False)

# 多类
class HeroInfo(models.Model):
    '''英雄人物模型表'''
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200,null=True,blank=True) # 控制后台管理输入框是否可为空白
    # 关系属性
    hbook = models.ForeignKey('BookInfo')
    # 删除标记
    isDeslete = models.BooleanField(default=False)