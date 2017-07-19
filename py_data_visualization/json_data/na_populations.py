"""
创建一副地图，显示三个北美国家的人口数量
"""

import pygal

wm = pygal.Worldmap()
wm.title = "Populations of Countries in North America"
# 传递字典，国别码为键，人口数为值。pygal根据数字大小自动着色
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')

