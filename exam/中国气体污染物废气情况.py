# -*- coding:utf-8 -*-

# 为了探索中国气体污染物废气情况，现调查了主要城市的废气中主要污染物排放情况，
# 包括2010年主要城市废气中主要污染物排放情况以及2014年主要城市废气中主要污染物排放情况，
# 以工业二氧化硫排放量为例，试比较是否排放量变高的现象，并给出检验统计量的值，alpha=0.05,使用配对数据检验方法

from scipy.stats import t
import numpy as np


class Solution():
	def solve(self):
		list_temp = ['6.0', '17.3', '104.3', '101.0', '120.4', '91.9', '30.0', '41.9', '23.9', '101.2', '67.7', '48.7', '39.9', '49.0', '136.6','117.6', '52.7', '64.9', '101.3', '83.5', '2.1', '58.6', '94.6', '62.4', '41.8', '0.2', '74.2', '40.1', '12.7', '27.8', '51.5']
		n = len(list_temp)
		list_old = []
		for i in range(n):
			list_old.append(float(list_temp[i])*10000)
		list_new = ['52041', '207793', '176469', '88880', '96190', '130672', '57246', '65987', '172867', '110665', '82021', '41483', '76043', '40756', '81118', '106123', '96222', '21173', '65589', '33045', '1798', '494415', '52040', '70603', '102842', '930', '69103', '72148', '71839', '92369', '74216']
		list_d = []
		for i in range(n):
			list_d.append((float(list_old[i]) - float(list_new[i])))

		average_d = np.mean(list_d)
		sum = 0.0;
		for k in n:
			sum += list_d[k];
		var_d = np.sqrt(sum / (n - 1))

		alpha = 0.05
		result = t.ppf(1 - alpha, n - 1)
		test = average_d / var_d * np.sqrt(n)

		if (result > test):
			return [test, 'NO']
		else:
			return [test, 'YES']

if __name__ == '__main__':
	S = Solution()
	print(S.solve())
