"""定义应用程序learning_notes的URL模式"""
# Django 的url函数
from django.conf.urls import url
# 本地项目的视图，用于映射本地URL到视图函数
from . import views

# 包含应用程序的URL模式的列表
urlpatterns = [
    # 项目主页的一个URL模式
    # Python忽略项目的基础URL,r'^$'直接匹配到基础URL;当请求的URL不与任何URL模式匹配时，Djang返回一个错误页面
    # Django会调用视图函数views.index()
    # name实参指定了这个URL模式的名称，以便能够在代码的其他地方引用它(index)
    url(r'^$', views.index, name='index'),

    # 呈现所有主题页面的URL模式
    url(r'^topics/$', views.topics, name='topics'),
    # 单个主题页面的URL模式
    # topic_id是一个实参,用于存储主题的id
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的网页URL
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面的URL模式
    # topic_id是一个存储与主题id匹配的数字的变量
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]

