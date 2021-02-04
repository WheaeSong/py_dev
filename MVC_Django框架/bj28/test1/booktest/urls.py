from django.conf.urls import url
from booktest import views

urlpatterns = [
        url(r'^index$',views.index),  # 建立/index和视图index之间的关系
        url(r'^index2$',views.index2),
        url(r'^books$',views.books), # 显示图书信息
        
        ]
