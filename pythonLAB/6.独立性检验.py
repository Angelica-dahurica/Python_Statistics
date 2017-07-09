# -*- coding: utf-8 -*-
'''
描述：
利用python实现简化版独立检验函数
输入：
A为二维数组，每行代表总体X的一个水平上的取值，每列代表总体Y的一个水平上的取值；
示例输入 : [[1.0,2.0,3.0],[2.0,2.0,3.0]]
输出：
[c-val,p-value]分别代表检验结果C值与其对应的P值；示例输出 : [0.257937,0.879002]
注意：
（1）A中只有一行时，返回结果为[0.0,None]
（2）结果保留6位小数点
'''
#公式参考教材第192页
from scipy.stats import chi2
class Solution():
    def independence_test(self, A):
        sizeH=len(A)
        if(sizeH==1):
            return [0.0,None]
        sizeL=len(A[0])

        total=0#全部数据的和
        for i in A:
            for j in i:
               total+=float(j)
        
        sumX=0
        sumY=0
        x=[]
        y=[]
        for i in range(sizeH):
            for j in range(sizeL):
                sumY+=float(A[i][j])
            x.append(sumY)
            sumY=0

        for i in range(sizeL):
            for j in range(sizeH):
                sumX+=float(A[j][i])
            y.append(sumX)
            sumX=0

        s=[]#表示偏差
        temp=[]
        for i in range(sizeH):
            for j in range(sizeL):
                t=x[i]*y[j]/total
                s3=((float(A[i][j])-t)**2)/t#偏差
                temp.append(s3)
            s.append(temp)
            temp=[]

        x2=0
        for i in s:
            for j in i:
                x2+=j
        x2=round(x2,6)
        p=chi2.sf(x2,(sizeH-1)*(sizeL-1))
        return [x2,p]
        
A=[[1.0,2.0,3.0],[2.0,2.0,3.0]]
#A=[[186,38,35],[227,54,45],[219,78,78],[355,112,140],[653,285,259]]       
a=Solution()
print(a.independence_test(A))
