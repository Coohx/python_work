from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习笔记的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回数据模型的字符串表示"""
        # Django调用方法__str__()返回属性text来表示关于“主题”的信息
        return self.text

