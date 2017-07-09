# -*- coding:utf-8 -*-

# 利用python实现简化版皮尔森相关系数计算函数
#
# 注意事项：
#
# 1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
#
# 2）x,y为空时，返回值为[None,None]
#
# 3）结果保留6位小数点

from scipy.stats import t
import math

class Solution():

    def pearsonr(self, x, y):
        n = len(x)
        if(n == 0):
            return [None, None]
        sum_x1 = 0
        sum_x2 = 0
        for i in x:
            sum_x1 += float(i)
            sum_x2 += float(i)**2
        sum_y1 = 0
        sum_y2 = 0
        for i in y:
            sum_y1 += float(i)
            sum_y2 += float(i)**2
        f1 = 0
        for i in range(n):
            f1 += float(x[i])*float(y[i])
        f1 = f1 * n
        f1 = f1 - sum_x1 * sum_y1
        f21 = (n * sum_x2-sum_x1**2)**0.5
        f22 = (n * sum_y2-sum_y1**2)**0.5
        f2 = f21 * f22
        r = f1 / f2
        r = round(r, 6)
        if(r == 1 or r == -1):
            p = 0
        else:
            T = r * ((n-2)/(1-r**2))**0.5
            p = t.sf(abs(T), (n-2)) * 2
            p = round(p, 6)
            print p
        return [r, p]

X=[1.0,2.0,3.0]
Y=[2.0,2.0,3.0]

S=Solution()
print(S.pearsonr(X,Y))