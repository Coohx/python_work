import json

import pygal
# 从模块style中导入控制颜色的样式RotateStyle(类),和加亮主题颜色的
#类LightColorizedStyle
#from pygal.style import RotateStyle, LightColorizedStyle
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

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

# 根据人口数量将所有的国家分成三大组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 显示每组分别包含多少个国家
#print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# 根据以上生成的字典绘制地图

# 创建样式类RotateStyle的实例,第一个参数是一个16进制的RGB颜色值;
#再传入参数base_style,指定基本样式,使用亮色的主题
wm_style = RS('#336699', base_style=LCS)
# 样式对象传递给要绘制的图表
wm = pygal.Worldmap(style=wm_style)
wm.title = 'World Population in 2010, by Country'
#wm.add('2010', cc_populations)
# add()根据不同的人口数,显示不同的颜色
wm.add('0-10M', cc_pops_1)
wm.add('10M-1Bn', cc_pops_2)
wm.add('>1Bn', cc_pops_3)

wm.render_to_file('world_population.svg')

