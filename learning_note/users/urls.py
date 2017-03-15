"""为应用程序users定义URL模式"""

from django.conf.urls import url
# 导入默认视图login
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登陆页面 http://localhost/users/下
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    # 注销URL:将请求发送给函数logout_view()
    url(r'^logout/$', views.logout_view, name='logout'),
    # 注册页面
    url(r'^register/$', views.register, name='register'),
]
