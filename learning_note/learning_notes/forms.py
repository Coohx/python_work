"""
Django 使用ModelForm类创建表单
    根据数据模型自动创建表单
"""
from django import forms

# 用于创建表单的数据模型
from .models import Topic

class TopicForm(forms.ModelForm):
    """主题表单"""
    class Meta:
        """管理表单的额外行为的元选项"""
        # 指定要创建表单的数据模型
        model = Topic
        # 表单包含的字段
        fields = ['text']
        # 字段标签为空
        labels = {'text': ''}

