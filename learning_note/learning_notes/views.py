from django.shortcuts import render

# Create your views here.
def index(request):
    """学习笔记的主页视图"""
    # 函数render()根据视图提供的数据渲染响应
    return render(request, 'learning_notes/index.html')

