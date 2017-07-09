# -*- coding: utf-8 -*-
'''
描述：
利用python实现简化版单总体T检验函数
输入：
a : 非空一维数组；popmean：假设总体期望值；示例输入 : [1.0,2.0,3.0],2.0
输出：
[t-val,p-value]分别代表检验结果T值与其对应的P值；示例输出 : [0.000000,1.000000]
注意：
（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
（2）结果保留6位小数点
'''
#公式参考教材第170页
import scipy.stats as sts
class Solution():
    def ttest_1samp(self, a, popmean):
        size=len(a)
        sum=0
        for i in a:
            sum+=float(i)
        mean=sum/size

        std=0
        for i in a:
            std+=(i-mean)**2
        std=(std/(size-1))**0.5

        t=(mean-popmean)/(std/((size)**0.5))
        p=sts.t.sf(abs(t),size-1)*2
        result=[]
        result.append(t)
        result.append(p)
        return result

a=[159,280,101,212,224,379,179,264,222,362,168,250,149,260,485,170]
popmean=225

A=Solution()
print(A.ttest_1samp(a,popmean))