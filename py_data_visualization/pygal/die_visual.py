r"""
"""
import pygal

from die import Die


# 创建一个骰子
die = Die()

# 存储掷骰子的结果
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 存储统计结果
frequencies = []

for value in range(1, die.num_sides+1):
    """按顺序统计每个点数出现的次数"""
    frequency = results.count(value)
    frequencies.append(frequency)

# 对统计结果可视化
# 创建一个Bar()实例
hist = pygal.Bar()

hist.title = "摇骰子1000次的结果"
#hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels = map(str, range(1, 7))
hist.x_title = "点数"
hist.y_title = "每个点数出现的次数"

# 指定值的标签, 要绘图的值"列表frequencies"
hist.add('6面骰子', frequencies)
# 将图表渲染为一个SVG文件
hist.render_to_file('die_visual.svg')

