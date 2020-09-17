import numpy as np

# numpy 中有着比 python 中更多的数据类型

# 1.获取数据类型的名称
# data_one = np.array([[1,2,3],[3,4,5]])
# print(data_one)
# # [[1 2 3]
# #  [3 4 5]]
# print(data_one.dtype)
# int32
# print(data_one.dtype.name)
# int32

# 2.转换数据类型
int_data = np.array([[1,2,3],[3,4,5]])

print(int_data.dtype)
# int32

float_data = int_data.astype(np.float64)
print(float_data.dtype)
# float64

















