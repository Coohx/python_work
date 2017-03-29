r"""
视图函数,处理http请求的数据，类似于CGI,
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
# 函数login_required()将作为装饰器
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """
    学习笔记的主页视图函数
    参数request是一个http请求对象
    """
    # 函数render()根据视图提供的数据渲染响应
    return render(request, 'learning_notes/index.html')

# 装饰器,先运行login_required()的代码,再运行topics()的代码
# login_required()检查用户是否登陆,仅当用户登录时Django才运行topics()的代码;
# 未登录时就重定向到登陆页面
@login_required
def topics(request):
    """显示所有的主题"""
    # 查询数据库,返回查询集(列表)，按添加时间排序
    # 用户登陆后,request对象将有一个user属性,存储了用户的信息
    # 方法filter()过滤出属主为登录用户的主题
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # 模板将使用字典数据用于生成网页
    contex = {'topics': topics}
    return render(request, 'learning_notes/topics.html', contex)

@login_required
def topic(request, topic_id):
    """
    显示单个主题及其所有的条目
    接受正则表达式(?P<topic_id>\d+)捕获的id,存在topic_id中
    """
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    check_topic_owner(request, topic)
    # 降序排列笔记条目
    entries = topic.entry_set.order_by('-date_added')
    # 主题&条目都存储在字典context中
    contex = {'topic': topic, 'entries': entries}
    # 将数据库中的内容context发送给模板topic.html
    return render(request, 'learning_notes/topic.html', contex)

@login_required
def new_topic(request):
    """
    添加新主题
    函数new_topic()将http请求对象作为参数
    保存新主题时,需要设置其属于当前登录用户,owner字段不能为空
    """
    if request.method != 'POST':
        # 未提交数据：创建一个新表单,即一个表单TopicForm类的实例
        form = TopicForm()
    else:
        # POST提交的数据,对数据(request.POST中)进行处理
        form = TopicForm(request.POST)
        # 检查数据的有效性
        if form.is_valid():
            # 先将新主题暂存,不存储到数据库,因为当前没有指定主题的属主
            new_topic = form.save(commit=False)
            # 将新主题的属主设置为当前登录用户
            new_topic.owner = request.user
            # 保存新主题到数据库
            new_topic.save()
            # 保存用户提交的数据后,将浏览器请求重定向到页面topics,查看新增的数据
            # 函数reverse()获取URL模式的URL
            return HttpResponseRedirect(reverse('learning_notes:topics'))
    # 存储表单数据
    context = {'form': form}
    return render(request, 'learning_notes/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """
    在特定的主题中添加新条目
    topic_id 用于存储从URL中获得的值
    """
    # 获取topic_id对应的正确主题
    topic = Topic.objects.get(id=topic_id)
    # 核实当前条目的主题关联的用户是否为当前登录用户
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # 新建一个条目对象(表单数据),将其存储到new_entry;
            # commit=False指定不将其保存到数据库
            new_entry = form.save(commit=False)
            # 设置当前提交的条目的主题(entry与topic分开存储到数据库,通过外键
            #关联)
            new_entry.topic = topic
            # 设置完新条目的主题后将其保存到数据库(注意条目与主题的存储逻辑)
            new_entry.save()
            # 将用户重定向到新增条目所属主题的页面
            # args列表包含重定向URL中的所有实参
            return HttpResponseRedirect(reverse('learning_notes:topic',
                                               args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_notes/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """
    编辑既有条目
        - 针对GET请求，返回一个表单，让用户对条目进行编辑;
        - 针对POST请求，将修改后的文本保存到数据库中
    """
    # 根据URL匹配到的条目ID获取用户要修改的条目对象
    entry = Entry.objects.get(id=entry_id)
    # 与要修改的条目关联的主题
    topic = entry.topic
    # 核实当前条目的主题关联的用户是否为当前登录用户
    check_topic_owner(request, topic)

    # 请求方法为GET
    if request.method != 'POST':
        """
        请求方法为GET，使用既有条目对象的内容创建一个表单，显示给用户，并能
        够编辑他们
        """
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_notes:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_notes/edit_entry.html', context)

def check_topic_owner(request, topic):
    """检查主题关联到的用户是否为当前登录用户"""
    if topic.owner != request.user:
        raise Http404

