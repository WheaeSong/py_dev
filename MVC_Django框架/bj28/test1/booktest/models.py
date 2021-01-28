from django.db import models
# 设计表对应的类
# Create your models here.

# 图书类
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20) # Charfiled说明是一个字符串，max_length指定最大长度
    # 出版日期，DateFiled说明是一个日期类型
    bpub_date = models.DateField()


# 英雄人物类
class Heroinfo(models.Model): 
    """
    英雄名：hname
    性别：hgender
    年龄：hage
    备注 ：hcomment
    关系属性： book建立图书类与英雄人物类一对多关系

    """
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    #  备注
    hcomment = models.CharField(max_length = 128)
    hbook = models.ForeignKey('BookInfo')
    
