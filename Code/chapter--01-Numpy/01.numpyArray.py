# 导入Numpy 工具包
import numpy as np
# 创建一个 3 行 4 列的数组
data = np.arange(12).reshape(3,4)
# 打印数组
print(data)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 查看 data 的类型
print(type(data)) # <class 'numpy.ndarray'>
# 数组维度的个数，
print(data.ndim) # 2. 表示 2 维数组
# 数组维度
print(data.shape) # (3, 4) 表示3 行 4 列的数组
# 数组元素的大小
print(data.size) # 12   3 行 4 列的数组里面有 12 个元素
# 数组元素的类型
print(data.dtype) # int32  表示元素类型都是 int32




