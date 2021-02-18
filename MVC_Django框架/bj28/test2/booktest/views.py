from datetime import date

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect # 重定向函数

# Create your views here.
from booktest.models import BookInfo


def index(request):
    '''显示图书信息'''
    # 1 查询所有图书信息
    books = BookInfo.objects.all()
    # 2 使用模板
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    '''下次你曾一本涂书'''
    # 1 新建bookinfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1999, 1, 1)
    # 保存今数据库
    b.save()
    # 3 返回应答，让浏览器在访问index
    '''重定向  使用重定向函数'''
    return redirect('/index')


def delete(request, bid):
    '''删除点击的图书'''
    # 通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 删除
    book.delete()
    # 重定向刀index
    return redirect('/index')
