"""
Django 使用ModelForm类创建表单
    根据models.py中的数据模型自动创建表单
"""
from django import forms

# 导入用于创建表单的数据模型
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """与模型Topic相关联的表单"""
    class Meta:
        """管理表单的额外行为的元选项"""
        # 指定要创建表单的数据模型
        model = Topic
        # 表单包含的字段
        fields = ['text']
        # 字段标签为空
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """与模型Entry相关联的表单"""
    class Meta:
        """管理表单这个实体本身属性的元选项"""
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 小部件widgets是一个HTML表单元素，如单行文本框、多行文本框、下拉列表
        # 设置属性widgets覆盖了Django的默认小部件
        # 类form.Textarea用来指定文本框的宽度(80)等属性
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

