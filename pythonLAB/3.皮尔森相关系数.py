#-*- coding:utf-8 -*-
'''
描述：
利用python实现简化版皮尔森相关系数计算函数
输入：
x : 一维数组；y : 一维数组，且x、y长度相同；示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]
输出：
[r-val,p-value]分别代表皮尔森相关系数、检验结果P值；示例输出 : [0.866025,0.333333]
注意：
（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
（2）x,y为空时，返回值为[None,None]
（3）结果保留6位小数点
'''
#公式参考教材第240页
#p值计算见241公式10.3
from scipy.stats import t
class Solution():
    def pearsonr(self, x, y):
        size=len(x)
        if(size==0):
            return [None,None]
        sumX=0
        sumX2=0
        for i in x:
            sumX+=float(i)
            sumX2+=float(i)**2
        sumY=0
        sumY2=0
        for i in y:
            sumY+=float(i)
            sumY2+=float(i)**2
        f1=0
        for i in range(size):
            f1+=float(x[i])*float(y[i])
        f1=f1*size
        f1=f1-sumX*sumY
        f21=(size*sumX2-sumX**2)**0.5
        f22=(size*sumY2-sumY**2)**0.5
        f2=f21*f22
        r=f1/f2
        r=round(r,6)
        if(r==1 or r==-1):
            p=0
        else:
            T=r*((size-2)/(1-r**2))**0.5
            p=t.sf(abs(T),(size-2))*2
            p=round(p,6)
        return [r,p]

X=[1.0,2.0,3.0]
Y=[2.0,2.0,3.0]

A=Solution()
print(A.pearsonr(X,Y))


