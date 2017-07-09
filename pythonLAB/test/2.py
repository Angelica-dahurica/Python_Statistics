# -*- coding: utf-8 -*-
'''
描述：
利用python实现化简版单因素方差检验函数
输入：
sample1,sample2,... : 不定数量（至少一个）的一维数组；示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]
输出：
[F-value, p-value]分别代表检验结果F值与其对应的P值；示例输出：[0.250000，0.643330]
注意：
（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
（2）sample_i为空时，返回值为[None,None]
（3）结果保留6位小数点
'''

#from scipy.stats import f
class Solution():
    def f_oneway(self, *args):
		size=len(args)
		if (size==0):
			return [None,None]
		total=0
		Qt=0
		n=0
		print args
		for i in args:
			r=len(i)
			if (r==0):
				return [None,None]
			for j in i:
				n+=1
				print j
				total+=float(j)
				Qt+=float(j)**2
			
		c=(total**2)/n
		St=Qt-c
		Qa=0
		for i in args:
			sum=0
			for j in i:
				sum+=float(j)
			Qa+=sum**2
		Qa=Qa/r
		Sa=Qa-c
		Se=St-Sa
		
		fa=size-1
		fe=n-size
		
		Va=Sa/float(fa)
		Ve=Se/float(fe)
		
		F=Va/Ve
		#p=f.sf(F,fa,fe)
		return F
		#return [F,p]
		

A=Solution()
args=[[25.6,22.2,28.0,29.8],[24.4,30.0,29.0,27.5],[25.0,27.7,23.0,32.2],[28.8,28.0,31.5,25.9],[20.6,21.2,22.0,21.2]]
print A.f_oneway(args)
