from django.contrib import admin

# Register your models here.

# 导入我们要注册的模型
from learning_notes.models import Topic, Entry

# Django通过管理网站管理我们的模型
admin.site.register(Topic)
admin.site.register(Entry)

