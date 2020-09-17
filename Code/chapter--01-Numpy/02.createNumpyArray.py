# 导入Numpy 工具包
import numpy as np

# 创建一个一维数组
data1 = np.array([1,2,3])
# print(data1)
# [1 2 3]

# 创建一个二维数组
data2 = np.array([[1,2,3],[4,5,6]])
# print(data2)
# [[1 2 3]
#  [4 5 6]]

# 通过 zeros 创建都是0的数组
zero = np.zeros((3,4))
# print(zero)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# 通过 ones 创建都是1 的数组
ones = np.ones((2,3))
# print(ones)
# [[1. 1. 1.]
#  [1. 1. 1.]]

#  通过 empty 创建一个新的数组，该数组只分配了内存空间，里面填充的元素都是随机的，而数据类型默认是 float64.
emptys = np.empty((2,3))
# print(emptys)
# [[4.45064003e-308 4.45047027e-308 1.95821982e-306]
#  [9.45734481e-308 4.45046008e-307 1.69120281e-306]]

# 通过 arrange 创建一个等差数组，第一个参数是数组初始的数值，第二个参数是数组中最大的数值，第三个参数是差值
arange = np.arange(2,20,5)
# print(arange)
# [ 2  7 12 17]












