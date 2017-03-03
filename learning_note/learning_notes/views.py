from django.shortcuts import render

from .models import Topic
# Create your views here.

# 服务器请求对象request
def index(request):
    """学习笔记的主页视图"""
    # 函数render()根据视图提供的数据渲染响应
    return render(request, 'learning_notes/index.html')

def topics(request):
    """显示所有的主题"""
    # 查询数据库，返回查询集(列表)，按添加时间排序
    topics = Topic.objects.order_by('date_added')
    # 模板将使用字典数据用于生成网页
    contex = {'topics': topics}
    return render(request, 'learning_notes/topics.html', contex)

