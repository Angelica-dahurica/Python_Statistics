# -*- coding:utf-8 -*-

# 当前世界全球变暖现象严重，为了探索中国是否也存在这个现象，现调查了中国主要城市的全年气温情况，
# 包括2010年全年气温状况与2014年全年气温状况，以8月份气温为例，假设主要城市温度符合正态分布，试比较是否存在温度上升现象？
# （需给出证明过程，仅回答YES或NO不得分）

from scipy.stats import t
import numpy as np
import urllib
import csv

class Solution():
	def solve(self):
		csv_reader = csv.reader(urllib.urlopen('http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv'))
		list_old = []
		for row in csv_reader:
			list_old.append(row[8])

		csv_reader = csv.reader(urllib.urlopen('http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv'))
		list_new = []
		for row in csv_reader:
			list_new.append(row[8])

		list_old = list_old[6:37]
		list_new = list_new[5:36]
		print list_old
		print list_new

		list_d = []
		for i in range(len(list_old)):
			list_d.append((float(list_old[i]) - float(list_new[i])))

		d_total = 0.0
		for i in range(len(list_d)):
			d_total += float(list_d[i])
		average_d = d_total / len(list_d)

		d = 0.0
		for nu in range(len(list_d)):
			d += (list_d[nu] - average_d) ** 2
		var_d = d / len(list_d)
		var_d = np.sqrt(var_d)

		alpha = 0.05
		n = len(list_d)
		result = t.ppf(alpha, n - 1)
		if(result>average_d/var_d*np.sqrt(n)):
			return 'YES'
		else:
			return 'NO'

if __name__ == '__main__':
	S = Solution()
	print(S.solve())
