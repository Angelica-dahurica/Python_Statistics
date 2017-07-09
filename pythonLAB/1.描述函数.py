#-*- coding:utf-8 -*-
'''
描述：
利用python实现简化版描述函数
输入：
a : 一维数组; 示例输入 : [1.0,2.0,3.0]
输出：
[mean,var,skew,kurt]分别代表均值、方差、偏度、峰度；示例输出 : [2.000000,1.000000,0.000000,-1.500000]
注意：
（1）不能调用math、scipy、numpy包
（2）数组只有一个元素时，方差值返回None
（3）结果保留6位小数点
'''

'''
要点：
1、方差为修正方差
2、偏度：分子：(xi-xAvg)^3/size,分母：((xi-xAvg)^2/size)^1.5
3、峰度：分子：(xi-xAvg)^4/size,分母：((xi-xAvg)^2/size)^2
4、对峰度进行减3的修正
5、计算偏度和峰度的时候，需要判断提供的数据是否只有一个，若只有一个，偏度为0，峰度为-3，否则会出现除数为0的错误
'''


class Solution():
    def describe(self, a):
        temp2=0
        temp3=0
        temp4=0
        size=len(a)
        sum=0
        for temp in a:
            sum+=float(temp)
        mean=sum/size

        for temp in a :
            temp2+=(float(temp) - mean) **2
            temp3+=(float(temp) - mean) **3
            temp4+=(float(temp) - mean) **4

        if(size==1):
            var=None
        else:
            var=temp2/(size-1)
            var=round(var,6)

        if (size!=1):
            f1=temp3/size
            f2=temp2/size
            f2=f2**1.5
            skew=f1/f2

            f3=temp4/size
            f4=temp2/size
            f4=f4**2
            kurt=f3/f4-3
        else:
            skew=0
            kurt=-3

        mean=round(mean,6) 
        skew=round(skew,6)
        kurt=round(kurt,6)
        result=[mean,var,skew,kurt]
        return result

A=Solution()
a=[1.0,2.0,3.0]
print(A.describe(a))
