from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """注销用户视图函数"""
    # 调用http请求给Django函数logout()
    logout(request)
    # 注销后重定向到主页
    return HttpResponseRedirect(reverse('learning_notes:index'))

def register(request):
    """
    注册新用户视图函数
    注册页面首次被请求(GET)时，显示一个空的注册表单;
    用户提交填写好的表单时(POST)对其进行处理
    """
    if request.method != 'POST':
        # 显示空的注册表单.使用Django的默认注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            # 如果用户提交的注册信息有效,
            # 调用方法save()将用户名&密码的散列值保存到数据库.
            # save()返回新创建的用户对象
            new_user = form.save()
            # 保存新用户的信息后,让用户自动登录，再重定向到主页
            # 用户名&密码无误后,返回一个通过了身份验证的用户对象
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_notes:index'))

    context = {'form': form}
    # 首次请求的是注册页面
    return render(request, 'users/register.html', context)

