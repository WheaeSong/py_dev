
from django.conf.urls import include, url
from django.contrib import admin
from booktest import views

urlpatterns = [

    url(r'^index$', views.index),  # 首页
    url(r'^showarg(\d+)',views.show_arg),  # 捕获url参数
]
