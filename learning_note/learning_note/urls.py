"""learning_note URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
"""管理项目中的所有url所需的函数&模块"""
from django.conf.urls import url, include
from django.contrib import admin

# 记录项目中所有apps的URL
urlpatterns = [
    # 模块admin.site.urls定义了管理网站的URL
    url(r'^admin/', admin.site.urls),
    # 添加应用程序learning_notes的URL
    url(r'', include('learning_notes.urls', namespace='learning_notes')),
    # 应用程序users的URL模式,匹配以‘users’打头的URL
    url(r'^users/', include('users.urls', namespace='users')),
]
