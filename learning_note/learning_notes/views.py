"""处理http请求的数据，类似于CGI"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm

# Create your views here.

# HTTP请求对象request看成一次http请求
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

def new_topic(request):
    """
    添加新主题
    函数new_topic()将http请求对象作为参数
    """
    if request.method != 'POST':
        # 未提交数据：创建一个新表单,即一个表单TopicForm类的实例
        form = TopicForm()
    else:
        # POST提交的数据,对数据(request.POST中)进行处理
        form = TopicForm(request.POST)
        # 检查数据的有效性
        if form.is_valid():
            # 将表单中的数据写入数据库
            form.save()
            # 保存用户提交的数据后,将浏览器请求重定向到页面topics,查看新增的数据
            # 函数reverse()获取URL模式的URL
            return HttpResponseRedirect(reverse('learning_notes:topics'))
    # 存储表单数据
    context = {'form': form}
    return render(request, 'learning_notes/new_topic.html', context)

