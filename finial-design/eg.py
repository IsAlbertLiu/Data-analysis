import pandas as pd
import numpy as np
#定义csv文件的位置
file_name = 'E:\\Data-analysis\\finial-design\\all.csv'
# 声明csv文件的路径，后面的参数是字符编码
file_path = open(file_name,'r', encoding='UTF-8')
# 将文件读入到DataFrame对象中
house_data = pd.read_csv(file_path)

# 输出对象
# print(house_data)

# 一：数据预处理
# 0.判断数据中是否有空值
# print(pd.isnull(house_data))
# 1. 检查缺失值和重复值。只要有重复的数据就会映射为 True
# print(house_data.duplicated())

# 2. 有重复的值，表明数据中有重复的数据。将重复的数据进行删除
# 删除重复的值，并对 house_data 重新赋值
# house_data = house_data.drop_duplicates()
# print(house_data)
# 3.检测数据中是否有缺失值，直接使用 dropna() 方法检测并删除的数据，
# 删除缺失的数据，并对 house_data 重新赋值。
# house_data = house_data.dropna()
# print(house_data) # 经过缺失数据检测之后，可以发现当前的数据总行数与之前相对比没有任何变化，因此，我们的数据中不存在缺失的数据。

# 4.查看数据维度、大小等基础信息
# print(house_data.ndim)  # 2 二维数组
# print(house_data.shape)  # (286, 5) 每个维度上数组的大小，表示一个 286 行 5 列的数组
# print(house_data.size)  # 1430 数组元素的总个数

# 二： 数据分析
# 1.使用 groupby 方法对数据进行分组
# print(house_data.groupby('地区'))
# print(house_data.groupby('地区').groups)
# print(house_data.groupby(['地区','小区']).groups)

# 2. 使用统计方法聚合数据
# print(house_data.groupby('地区').mean()) # 按照地区进行分组，计算出面积以及价格的平均值
# 对每列使用不同的函数聚合分组数据
print(house_data.agg({'面积':sum,'价格':sum}))  # 面积    16038 价格    296338  dtype: int64


# 三： 图表分析

# 对特征数据进行提取
# 对地区进行提取
# print(house_data['地区'].unique())  # ['江岸' '洪山' '武昌' '江汉' '沌口开发区' '青山' '蔡甸' '黄陂' '东西湖' '汉阳' '江夏' '东湖高新' '硚口' '新洲']
# print(house_data['小区'].unique()) # 对小区进行数据提取
# print(house_data['户型'].unique()) # 对户型进行数据提取

# # 对房屋价格和面积进行分析提取
print('房屋最大面积是%d平方米' % (house_data['面积'].max()))
print('房屋最小面积是%d平方米' % (house_data['面积'].min()))
print('房屋最高价格为每月%d元' % (house_data['价格'].max()))
print('房屋最低价格为每月%d元' % (house_data['价格'].max()))


def all_house(arr):
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result

house_array = house_data['户型']
house_info = all_house(house_array)
print(house_info)

# 使用字典推导式，将数量大于 10 的类型全部输出
house_type = dict((key, value) for key, value in house_info.items() if value > 10)
show_houses = pd.DataFrame({
    '户型': [x for x in house_type.keys()],
    '数量': [x for x in house_type.values()],
})
print(show_houses)

# ## 进行绘制
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
house_type = show_houses['户型']
house_type_num = show_houses['数量']
plt.barh(range(11),house_type_num,height=0.7,color='steelblue',alpha=0.8)
plt.yticks(range(11),house_type)
plt.xlim(0,100)
plt.xlabel("数量")
plt.ylabel("户型种类")
plt.title("武汉地区各户型房屋数量")
for x,y in enumerate(house_type_num):
    plt.text(y+0.2,x-0.1,'%s'%y)
plt.show()

#

#
# 将房屋面积按照 6 个区间进行划分
area_divide = [1,30,50,70,90,110,130,1200]
area_cut = pd.cut(list(house_data['面积']), area_divide)
area_cut_data = area_cut.describe()
print(area_cut_data)

# 绘制饼图
area_percentage = (area_cut_data['freqs'].values)*100
labels = ['30平方米以下','30-50平方米','50-70平方米','70-90平方米','90-110平方米','110-130平方米','130-1200平方米']
plt.axes(aspect=1)
plt.pie(x=area_percentage,labels=labels,autopct='%.2f %%',shadow=True,labeldistance=1.2,startangle=90,pctdistance=0.7)
plt.legend(loc = 'upper right')
plt.show()







