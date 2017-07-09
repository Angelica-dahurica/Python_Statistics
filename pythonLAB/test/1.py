#-*- coding:utf-8 -*-
'''
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

class Solution():
    def describe(self, a):
		sum=0
		n=len(a)
		for i in a:
			sum +=float(i)
		mean=sum/n
		
		var=0
		if(n==1):
			var=None
		else:
			for i in a:
				var+=(float(i)-mean)**2
			var=var/(n-1)
		
		if(n!=1):
			temp2=0
			temp3=0
			temp4=0
			for i in a:
				temp2+=(float(i)-mean)**2
				temp3+=(float(i)-mean)**3
				temp4+=(float(i)-mean)**4
			temp2=temp2/n
			temp3=temp3/n
			temp4=temp4/n
			
			skew=(temp3)/(temp2)**1.5
			kurt=(temp4)/(temp2)**2-3
		else:
			skew=0
			kurt=-3
		
		return [mean, var, skew, kurt]
		
A=Solution()
a=[1.0,2.0,3.0]
print A.describe(a)