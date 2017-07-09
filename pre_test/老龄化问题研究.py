# -*- coding:utf-8 -*-

# 人口普查是一项重要的国情调查，对于国家管理、制定各项方针政策具有重要的意义，中国最早的一次人口普查在西汉汉平帝元始二年进行，
# 而自中华人民共和国建国以来分别在1953、1964、1982、1990、2000和2010年进行了共六次人口普查，
# 其中第六次人口普查分别涉及到了人口增长、家庭户人口、性别构成、年龄构成、民族构成、受教育程度、城乡人口、人口流动性等八方面。
# 现有《各地区分性别、健康状况的60岁及以上老年人口》调查数据、《各地区户数、人口数和性别比》调查数据，定义老龄率=60岁及以上人口数*100/总人口数，
# 以北京市为例，其老龄率为250084*100/1849475=13.52，请编写python代码回答如下问题：
# 以各省市数据为代表，求取中国省级老龄率均值的置信区间、方差的置信区间，置信水平均为90%，假设老龄率符合正态分布


from scipy.stats import norm
from scipy.stats import chi2
import numpy as np
import csv
import urllib


class Solution():
	def solve(self):
		# 打开本地csv
		# csv_reader = csv.reader(open('population_old.csv'))
		csv_reader = csv.reader(urllib.urlopen('http://py.mooctest.net:8081/dataset/population/population_old.csv'))
		list_old = []
		for row in csv_reader:
			list_old.append(row[1])

		csv_reader = csv.reader(urllib.urlopen('http://py.mooctest.net:8081/dataset/population/population_total.csv'))
		list_total = []
		for row in csv_reader:
			list_total.append(row[4])

		list_old = list_old[3:]
		list_total = list_total[5:]
		list_rate = []
		for i in range(len(list_old)):
			list_rate.append(float(list_old[i]) * 100 / float(list_total[i]))

		n = len(list_rate)

		num = 0.0
		for number in range(n):
			num += list_rate[number]
		average = num / len(list_rate)

		d = 0.0
		for nu in range(n):
			d += (list_rate[nu] - average)**2
		var = np.sqrt(d / len(list_rate))

		alpha = 0.1
		test = norm.ppf(1 - alpha / 2)
		aver_lower = average - var / np.sqrt(n) * test
		aver_higher = average + var / np.sqrt(n) * test

		var_lower = ((n - 1) * var**2) / chi2.ppf(1 - alpha / 2, n - 1)
		var_higher = ((n - 1) * var ** 2) / chi2.ppf(alpha / 2, n - 1)
		return [[aver_lower, aver_higher], [var_lower, var_higher]]

if __name__ == '__main__':
	S = Solution()
	print(S.solve())
