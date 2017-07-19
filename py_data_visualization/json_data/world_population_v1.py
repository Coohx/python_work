import json

import pygal

# 导入国别码提取函数
from country_codes import get_country_code

# 通过json.load()载入列表数据
filename = 'population_data.json'
with open(filename) as f:
    # 存储列表数据
    pop_date = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
# 列表中的每个元素都是一个字典,有四个键,依次存储在pop_dict中
for pop_dict in pop_date:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        # 从json文件中获取国家人口数,int型存储
        population = int(float(pop_dict['Value']))
        #print(country_name + ": " + str(population))
        # 获取国别码,有则存储在code中,没有则存储None
        code = get_country_code(country)
        if code:
            # 将国别码作为键,人口数作为值,填充新的字典,用于pygal绘制人口地图
            cc_populations[code] = population

# 根据以上生成的字典绘制地图
wm = pygal.Worldmap()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')

