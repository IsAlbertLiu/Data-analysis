import pandas as pd
import numpy as np

file_path = open('E:\\Data-analysis\\finial-design\\DataSet\\mtcars.csv')
file_data = pd.read_csv(file_path) # 将文件读入到DataFrame对象中

# print(file_data)  # 输出对象

# -----------数据预处理
# 1. 检查缺失值和重复值。只要有重复的数据就会映射为 True
print(file_data.duplicated())

# 2. 有重复的值，表明数据中有重复的数据。将重复的数据进行删除
file_data = file_data.drop_duplicates()  # 删除重复的值，并对 file_data 重新赋值
print(file_data)
# 3.检测数据中是否有缺失值，直接使用 dropna() 方法检测并删除的数据，
file_data = file_data.dropna()  # 删除缺失的数据，并对 file_data 重新赋值。
print(file_data) # 经过缺失数据检测之后，可以发现当前的数据总行数与之前相对比没有任何变化，因此，我们的数据中不存在缺失的数据。

#  4. 图表分析      分析：1.将总马力进行分类
#  4.1 获取每个汽车的种类


def all_type_cars(arr):
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result

# 获取车辆类型的数据
cars_array = file_data['type']
cars_info = all_type_cars(cars_array)
print(cars_info)

# 使用字典推导式，将数量大于 50 的类型全部输出


