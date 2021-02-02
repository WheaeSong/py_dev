from django.contrib import admin
from booktest.models import BookInfo,Heroinfo
# Register your models here.
# 后台管理及相关文件
# 注册模型类
class BookInfoAdmin(admin.ModelAdmin):
    # 图书模型管理类
    list_display = ['id','btitle','bpub_date']
    # 注册模型类

class HeroinfoAdmin(admin.ModelAdmin):
    '''英雄模型管理类'''
    list_display = ['hname','hgender','hcomment']
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(Heroinfo,HeroinfoAdmin)


