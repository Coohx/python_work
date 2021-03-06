#!/usr/bin/env python3
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """用户学习笔记的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # 关联到User表的外键,将主题关联到提交它的用户
    owner = models.ForeignKey(User)

    def __str__(self):
        """返回数据模型的字符串表示"""
        # Django调用方法__str__()返回属性text来表示关于“主题”的信息
        return self.text

class Entry(models.Model):
    """主题下面的条目内容,按添加时间存储在数据库中"""
    # 数据库外键，引用了表Topic中的一条记录，关联到特定的主题
    topic = models.ForeignKey(Topic)
    # TextField()字段不需要长度限制
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """数据模型Entry的额外属性的元选项"""
        # 指定条目标题的显示格式
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        # 对字符串进行切片，只显示前50个字符，外加省略号
        if len(self.text) >= 50:
            return self.text[:50] + "..."
        else:
            return self.text

