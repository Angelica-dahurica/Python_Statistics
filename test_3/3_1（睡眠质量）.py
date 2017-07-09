# -*- coding:utf-8 -*-

# 随着中国经济发展，人们生活质量相应提升，但睡眠质量却并不乐观。
# 据《2016中国睡眠指数报告》显示，中国人平均睡眠时长为8.5小时， 这是从3600份问卷统计得到的结果。
# 另外报告指出，中国人睡眠时长符合方差为25的正态分布，试写solve函数估计中国人睡眠时长的置信区间(置信水平为95%)
# [lower,upper]分别代表睡眠时长的估计下限与上限

import numpy as np
from scipy.stats import norm

# 单总体均值区间估计P144


class Solution:

    @staticmethod
    def solve():
        alpha = 0.05
        test = norm.ppf(1 - alpha / 2)
        mean = 8.5
        n = 3600
        var = np.sqrt(25)
        lower = mean - var / np.sqrt(n) * test
        upper = mean + var / np.sqrt(n) * test
        return [lower, upper]

if __name__ == '__main__':
    S = Solution()
    print(S.solve())
