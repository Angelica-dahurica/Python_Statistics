# -*- coding: utf-8 -*-
'''
描述：
利用python实现简化版单因素方差检验函数
输入：
sample1,sample2,... : 不定数量（至少一个）的一维数组；示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]
输出：
[F-value, p-value]分别代表检验结果F值与其对应的P值；示例输出：[0.250000，0.643330]
注意：
（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
（2）sample_i为空时，返回值为[None,None]
（3）结果保留6位小数点
'''

#公式参考教材第213-215页
import scipy.stats as sts
class Solution():
    def f_oneway(self, *args):
        n=0
        sum=0
        Qt=0
        if(len(args)==0):
            return [None,None]
        for i in args:
            if(len(i)==0):
                return [None,None]
            for j in i:
                sum+=float(j)
                n+=1
                Qt+=j**2

        C=sum**2/n
        St=Qt-C

        Qa=0
        r=0;
        for i in args:
            r=len(i)
            total=0
            for j in i:
                total+=float(j)
            Qa+=total**2

        Qa=Qa/r
        Sa=Qa-C

        Se=St-Sa

        m=len(args)
        fa=m-1
        fe=n-m

        Va=Sa/fa
        Ve=Se/fe

        Fa=Va/Ve
        p=sts.f.sf(Fa,fa,fe)
        Fa=round(Fa,6)
        p=round(p,6)
        return [Fa,p]
        
arg=[[25.6,22.2,28.0,29.8],[24.4,30.0,29.0,27.5],[25.0,27.7,23.0,32.2],[28.8,28.0,31.5,25.9],[20.6,21.2,22.0,21.2]]
A=Solution()
print A.f_oneway(arg)

