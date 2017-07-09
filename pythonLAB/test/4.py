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
#from scipy.stats import t
class Solution():
	def ttest_1samp(self, a, popmean):
		avg = self.getAvg(a)
		s = self.getS(avg,a)
		n = len(a)

		x = (avg-popmean)/(s/(n**0.5))
		print x

	def getAvg(self, a):
		total = 0
		n = len(a)
		for i in a:
			total += float(i)
		return total / n

	def getS(self, avg, a):
		var = 0
		n = len(a)
		for i in a:
			var += (float(i)-avg)**2
		var = var / (n - 1)
		s = var**0.5
		return s


a = [1.0, 2.0, 3.0]
popmean = 2.0

A = Solution()
print A.ttest_1samp(a,popmean)