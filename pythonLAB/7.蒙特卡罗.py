#-*- coding:utf-8 -*-
'''
描述：
蒙特卡罗方法，或称计算机随机模拟方法，是一种基于随机数的计算方法，在金融工程学，宏观经济学，计算物理学等领域应用广泛。
试编写函数solve(a,b)，利用蒙特卡罗方法计算函数f(x)=(e^(-x²/2))/√2√π在区间[a,b]上的定积分并返回，其中b>a>0。
输入：
a,b分别为正浮点数
输出：
m: 定积分值
注意：
（1）为保证精确性，蒙特卡罗模拟次数至少为100000
（2）不能使用scipy.integrate库
'''
'''
微元法求积分
将积分区间均分，从a加到b，每次累加等dirta长度
在累加的过程中，将结果每次加上dirta长度*f(x)的值
累加完毕后返回结果
'''

from math import e
from math import pi

class Solution():
    def solve(self,a,b):
        dirta=(float(b)-float(a))/100000
        i=0
        result=0
        
        while((a+i*dirta)<b):
            result+=dirta*self.f(a+i*dirta)
            i+=1
        
        return result

    def f(self,x):
        fx=0
        zhishu=-(x**2)/2
        f1=e**zhishu
        f2=(2**0.5)*(pi**0.5)
        fx=float(f1)/f2
        return fx
A=Solution()
a=2
b=5
print(A.solve(a,b))

