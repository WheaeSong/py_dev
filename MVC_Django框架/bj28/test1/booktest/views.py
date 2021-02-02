from django.template import loader,RequestContext
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 1 定义视图函数: HttpRequest
# 2 进行URL配置 http:127.0.0.1：8000/index，建立视图与url地址的对应关系



def my_render(request,templates_path,context_dict={}):
    #return HttpResponse('老铁，没毛病')    
    # 使用模板
    # 1 加载模板文件内容,模板对象
    temp = loader.get_template(templates_path)
    # 定义模板上下文
    context= RequestContext(request,context_dict)
    # 3 模板渲染产生标准的html内容
    res_html = temp.render(context)
    # 返回给浏览器
    return HttpResponse(res_html)



def index(request):
    # 进行处理，与M和T交互
    return render(request,'booktest/index.html',{'content': "hello world"})
        


def index2(request):
    return HttpResponse('hello python')
