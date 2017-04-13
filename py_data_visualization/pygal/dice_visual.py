r"""
"""
import pygal

from die import Die


# 创建两个骰子
die_1 = Die()
die_2 = Die(10)

# 存储两次投掷骰子的结果和
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 存储统计结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    """按顺序统计每个点数出现的次数"""
    frequency = results.count(value)
    frequencies.append(frequency)

# 对统计结果可视化
# 创建一个Bar()实例
hist = pygal.Bar()

hist.title = "每次掷一个6面骰子&10面的骰子，掷5000次的和的分布情况"
#hist.x_labels = ['1', '2', '3', '4', '5', '6']
#hist.x_labels = map(str, range(2, max_result+1))
# 坐标轴标签为字符型
hist.x_labels = [str(x_label) for x_label in range(2, max_result+1)]
hist.x_title = "点数"
hist.y_title = "每个点数出现的次数"

# 指定值的标签, 要绘图的值
hist.add('D6 + D10骰子的和', frequencies)
# 将图表渲染为一个SVG文件
hist.render_to_file('die_visual.svg')

