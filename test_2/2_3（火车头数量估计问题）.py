# -*- coding:utf-8 -*-
# 铁路公司将它所有的火车头都进行了编号，从1到N。有一天你看见一个编号为60的火车头，那该铁路公司共有多少火车头呢？
# 试用极大似然估计、最小偏方差估计、无偏估计分别估算火车头数目x，并重复10000次试验，计算命中率、均偏方差(x-N)^2、均偏差(x-N)并进行比较，
# 体会各种估计方法的优缺点。
# 下面为火车头问题的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）假如你看到了两辆火车，编号分别为46、24，那么如何进行参数估计呢？（提示：多次估算计算平均值or修改估算公式？）
# （3）假如你看到了多辆（多于两辆）火车呢？

# -*- coding:utf-8 -*-
import random


def number_trans(upper_bound):
	return random.randint(1, upper_bound)  # 随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值


def train_seen(n):
	return random.randint(1, n)


def mle_estimation(evidence):  # Maximum Likelihood Estimate 极大似然估计
	return evidence


def mse_estimation(evidence):  # 最小偏方差估计
	return round(1.5 * evidence)


def me_estimation(evidence):  # 无偏估计
	return 2 * evidence


def estimate():
	number_experiments = 10000
	upper_bound = 100
	h1 = h2 = h3 = mse1 = mse2 = mse3 = me1 = me2 = me3 = 0.0

	for j in range(number_experiments):
		# 返回一个1-100的数作为实际火车头数
		n = number_trans(upper_bound)
		# 看到的火车头数（题目中为60）
		evidence = train_seen(n)

		hypo1 = mle_estimation(evidence)
		hypo2 = mse_estimation(evidence)
		hypo3 = me_estimation(evidence)
		# calculating hits
		h1 = h1 + 1 if hypo1 == n else h1
		h2 = h2 + 1 if hypo2 == n else h2
		h3 = h3 + 1 if hypo3 == n else h3

		# calculating mean squared error
		mse1 += (hypo1 - n) ** 2
		mse2 += (hypo2 - n) ** 2
		mse3 += (hypo3 - n) ** 2

		# calculating mean error
		me1 += (hypo1 - n)
		me2 += (hypo2 - n)
		me3 += (hypo3 - n)

	print(h1 / number_experiments)
	print(h2 / number_experiments)
	print(h3 / number_experiments)
	print(mse1 / number_experiments)
	print(mse2 / number_experiments)
	print(mse3 / number_experiments)
	print(me1 / number_experiments)
	print(me2 / number_experiments)
	print(me3 / number_experiments)


# the code should not be changed
if __name__ == '__main__':
	estimate()
