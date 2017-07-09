#-*- coding:utf-8 -*-
'''
描述：利用python实现简化版皮尔森相关系数计算函数
输入：x : 一维数组；y : 一维数组，且x、y长度相同；
示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]
输出：[r-val,p-value]分别代表皮尔森相关系数、检验结果P值；
示例输出 : [0.866025,0.333333]
注意：
（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
（2）x,y为空时，返回值为[None,None]
（3）结果保留6位小数点
'''
'''
要点：
1.p-value的求法
	当abs(r)==1的时候，p-value应当为0
	else:
		t=r*(((n-2)/(1-r**2))**0.5)
		p=scipy.stats.t.sf(abs(t),n-2)*2.0
'''
from scipy.stats import t
class Solution():
	def pearsonr(self, x, y):
		n=len(x)
		if(n==0):
			return [None,None]
		else:
			sumX=0
			sumY=0
			sumX2=0
			sumY2=0

			sumX=self.getSum(x)
			sumX2=self.getSum2(x)
			sumY=self.getSum(y)
			sumY2=self.getSum2(y)

			xy=0
			for i in range(n):
				xy+=float(x[i])*float(y[i])
			f1=n*xy-sumX*sumY
			f21=(n*sumX2-sumX**2)**0.5
			f22=(n*sumY2-sumY**2)**0.5
			f2=f21*f22
			if(f2==0):
				return [None,None]
			r=f1/f2
			r=round(r,6)

			if(r==1 or r==-1):
				p=0
			else:
				T=r*((n-2)/(1-r**2))**0.5
				p=t.sf(abs(T),n-2)*2
				p=round(p,6)

			return [r,p]

	
	def getSum(self,x):
		sumX=0
		for i in x:
			sumX+=float(i)
		return sumX

	def getSum2(self,x):
		sumX2=0
		for i in x:
			sumX2+=float(i)**2
		return sumX2

a=Solution()
print a.pearsonr([1.0,2.0,3.0],[2.0,2.0,3.0])