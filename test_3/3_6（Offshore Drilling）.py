# -*- coding:utf-8 -*-


# The table below summaries a data set that examines the response of a random sample of college graduates and non-graduate on the topic of oil drilling. 
# Complete a chi-square test for test data to check whether there is a statistically significant difference in responses from college graduates and non-graduates.
# College Grad? Yes  No   Total
# Support       154  132  286
# Oppose        180  126  306
# Do not know   104  131  235
# Total         438  389  827

import numpy as np
from scipy.stats import chi2


# 卡方独立性检验P191


class Solution():

	@staticmethod
	def solve():
		[result, test] = chi2_independance([154, 180, 104], [132, 126, 131])
		return [2, round(result, 2) + 0.01, test > result]


def chi2_independance(*arg):
	c = len(arg)
	r = len(arg[0])
	arg = np.array(arg)
	row = list(sum(arg))
	col = [sum(arg[i]) for i in xrange(c)]
	total = float(sum(row))
	result = 0
	for i in xrange(c):
		for j in xrange(r):
			result += (arg[i][j] - col[i] * row[j] / total) ** 2 / (col[i] * row[j] / total)
	test = chi2.ppf(0.05, (r - 1) * (c - 1))
	return [result, test]

if __name__ == '__main__':
	S = Solution()
	print(S.solve())
