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

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    """
    接受正则表达式(?P<topic_id>\d+)捕获的id,存储到topic_id中
    """
    topic = Topic.objects.get(id=topic_id)
    # 降序排列笔记条目
    entries = topic.entry_set.order_by('-date_added')
    # 主题&条目都存储在字典context中
    contex = {'topic': topic, 'entries': entries}
    # 将数据库中的内容context发送给模板topic.html
    return render(request, 'learning_notes/topic.html', contex)
