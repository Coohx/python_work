# http请求包
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# 将响应对象存储在变量r中
r = requests.get(url)
# 输出响应对象的状态码属性
print("Status code:", r.status_code)

# 将API响应内容(JSON格式信息)转换为字典,存储在变量中
response_dict = r.json()
# 打印API调用返回的字典中的总仓库数
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
# 与键‘items’相关联的值是一个列表,包含很多字典,每个字典都包含有关一个Python仓库的信息
repo_dicts = response_dict['items']

# 存储将要包含在图表中的信息('项目名'用于给条形加上标签,'星'用于确定条形的高度)
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
print(names)

# 可视化
# 基色深蓝色,基本样式LCS
my_style = LS('#333366', base_style=LCS)
# Bar()创建一个条形图对象,标签绕x轴旋转45度,隐藏图例
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Started Python Project on Github'
# x轴标签设置为列表names
chart.x_labels = names

# 添加数据
# 数据的标签设置为空字符''
chart.add('', stars)
chart.render_to_file('python_repos.svg')

