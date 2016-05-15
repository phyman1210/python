# coding: utf-8
import numpy as np

a = np.arange(4).reshape(2,2)
print(a)

b = np.arange(3,7).reshape(2,2)
print(b)

print(a+b)
print(a.T)
print(a.T + b)
print(a-b)
print(np.dot(a,b))

c = np.arange(10)
print(c)

# インデグシング
ii = np.array([2,5])
print(c[ii])

# スライシング
print(c[3:6])

# ブロードキャスティング
print(np.exp(c))

# 行列の結合
d = np.arange(3)
e = np.arange(3, 6)
print(np.c_[d,e])
print(np.r_[d,e])
