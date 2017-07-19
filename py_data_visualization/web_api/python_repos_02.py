# http请求包
import requests

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
# 打印字典列表的长度,获悉我们获得了多少个仓库的信息
print("Repositories returned:", len(repo_dicts))

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    # 项目所有者字典repo_dict['owner'],此处为嵌套字典,键login获取所有者的登录名
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Descriotion:', repo_dict['description'])

