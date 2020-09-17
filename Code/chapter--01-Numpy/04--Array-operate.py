import numpy as np

# 1.矢量化运算
data1 = np.array([[1,2,3],[4,5,6]])
data2 = np.array([[1,2,3],[4,5,6]])

# 数组相加
print(data1+data1)
# [[ 2  4  6]
#  [ 8 10 12]]

# 数组相减
print(data1-data1)
# [[0 0 0]
# [0 0 0]]

# 数组相乘
print(data1*data1)
# [[ 1  4  9]
# [16 25 36]]

# 数组相除
print(data1/data1)
# [[1. 1. 1.]
# [1. 1. 1.]]

# 2.数组广播
arr1 = np.array([[1],[2],[3],[4]]) # 创建了一个二维数组，
arr2 = np.array([1,2,3])

print(arr1.shape)
# array[0][0]=1	array[0][1]=2	array[0][2]=3	array[0][3]=4
# (4, 1)

print(arr1+arr2)
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]
#  [5 6 7]]

# 为什么结果会是这样？
# 两个形状不相等的数组进行运算的时候，会进行补位。
# 第一个数组会变成
# array[0][0]=1	array[0][1]=2	array[0][2]=3	array[0][3]=4
# array[1][0]=1	array[1][1]=2	array[1][2]=3	array[1][3]=4
# array[2][0]=1	array[2][1]=2	array[2][2]=3	array[2][3]=4

# 第二个数组会变成
# array[0][0]=1	array[0][1]=1	array[0][2]=1	array[0][3]=1
# array[1][0]=2	array[1][1]=2	array[1][2]=2	array[1][3]=2
# array[2][0]=3	array[2][1]=3	array[2][2]=3	array[2][3]=3


# 3.数组与标量之间的运算
da1 = np.array([[1,2,3],[4,5,6]])
da2 = 10

# 数组与标量相加
print(da1+da2)
# [[11 12 13]
# [14 15 16]]

# 数组与标量相减
print(da1-da2)
# [[-9 -8 -7]
# [-6 -5 -4]]

# 数组与标量相乘
print(da1*da2)
# [[10 20 30]
# [40 50 60]]

# 数组与标量相除
print(da1/da2)
# [[0.1 0.2 0.3]
# [0.4 0.5 0.6]]



