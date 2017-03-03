"""定义应用程序learning_notes的URL模式"""
# Django 的url函数
from django.conf.urls import url
# 本地项目的视图，用于映射本地URL
from . import views

# 包含应用程序的URL模式的列表
urlpatterns = [
    # 项目主页的一个URL模式
    # Python忽略项目的基础URL,r'^$'直接匹配到基础URL;当请求的URL不与任何URL模式匹配时，Djang返回一个错误页面
    # Django会调用视图函数views.index()
    # name实参指定了这个URL模式的名称，以便能够在代码的其他地方引用它(index)
    url(r'^$', views.index, name='index'),

    # “学习笔记”主题的URL模式
    url(r'^topics/&', views.topics, name='topics'),
]
