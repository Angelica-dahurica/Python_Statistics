# -*- coding:utf-8 -*-

# 假定一块蛋糕上的葡萄干粒数服从泊松分布，如果想让每块蛋糕上至少有一粒葡萄干的概率大于等于0.98，蛋糕上葡萄干的平均粒数应该是多少？


# -*- coding:utf-8 -*-
import numpy as np

class Solution():
	def solve(self):
		for i in range(10):
			result = np.e ** -int(i)
			if result <= 0.02:
				return i

		# p = 0.02
		# aver = -np.log(p)
		# return int(round(aver, 0))

if __name__ == '__main__':
	S = Solution()
	print(S.solve())
