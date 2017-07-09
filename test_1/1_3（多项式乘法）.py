# -*- coding:utf-8 -*-
# 在Numpy中，多项式函数的系数可以用一维数组表示，例如对于f(x)=2x^3-x+1可表示为f=np.array([2.0,0.0,-1.0,1.0])，
# 而np.poly1d()方法可以将多项式转换为poly1d(一元多项式)对象，返回多项式函数的值，
# 请利用poly1d()方法计算多项式g(x)(例如g(x)=x^2+2x+1)和f(x)的乘积并将结果返回


import numpy as np

class Solution():
	def solve(self, A):
		result = []

		listf = [2.0,0.0,-1.0,1.0]
		listg = []

		#返回各项系数
		tmp = np.poly1d(A).coeffs

		lenf = len(listf)
		leng = len(tmp)

		if(leng >= lenf):
			for i in range(0,leng-lenf):
				listf.insert(i,0)
			for i in range(leng-lenf,leng):
				listf.insert(i,tmp[i-leng+lenf])

			for i in range(0,leng*2-1):
				result.insert(i,0)

			for i in range(0, leng):
				for j in range(0,leng):
					result[i+j] = listg[i] * listf[j] + result[i+j]
		else:
			for i in range(0,lenf-leng):
				listg.insert(i,0)
			for i in range(lenf-leng,lenf):
				listg.insert(i,tmp[i-lenf+leng])

			for i in range(0,lenf*2-1):
				result.insert(i,0)

			for i in range(0, lenf):
				for j in range(0,lenf):
					result[i+j] = listg[i] * listf[j] + result[i+j]

		#np.array(result)将列表转换为array
		return np.poly1d(np.array(result))


solution = Solution()
g=np.array([1.0, 2.0, 1.0])
print(solution.solve(g))
