import pygal

# 创建一个地图实例
wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'

# add()接受一个标签和一个列表(包含有国家码).每次调用add()都将为指定的国家选择一
# 种颜色
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe',
                         'py', 'sr', 'uy', 've'])

# 将地图图表保存为svg图片
wm.render_to_file('america.svg')
