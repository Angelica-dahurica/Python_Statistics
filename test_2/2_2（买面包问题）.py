# -*- coding:utf-8 -*-
# 下面为庞加莱买面包问题的python实现代码，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）比较first_year与second_year结果，特别是平均值和偏度，看看有无出入？

import numpy
import scipy.stats as sta
import matplotlib.pyplot as plt


def first_year():
	# generate random data in normal distribution whose expectation(数学期望) is 950 and standard deviation(标准差) is 20
	data = sta.norm(loc=950, scale=20)

	wbread = []
	for i in range(365):
		x = data.rvs(size=100)  # Generate random numbers
		wbread.append(x[0])  # get the random data for one day

	print(numpy.mean(wbread))  # print mean value
	print(sta.skew(wbread))  # print skew value
	plt.hist(wbread, color='grey')  # generate histogram（直方图)
	plt.savefig('first_year.png')  # save figure


def second_year():
	data = sta.norm(loc=950, scale=20)

	wbread = []
	for i in range(365):
		x = data.rvs(size=100)
		wbread.append(max(x))  # get the random data for one day

	print(numpy.mean(wbread))  # print mean value
	print(sta.skew(wbread))  # print skew value
	plt.hist(wbread, color='grey')
	plt.savefig('second_year.png')

# the code should not be changed
if __name__ == '__main__':
	first_year()
	second_year()
