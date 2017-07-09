# -*- coding:utf-8 -*-

# A 95% confidence interval for a population mean, u, is given as (18.985, 21.015).
# This confidence interval is based on a simple random samples of 36 observations.
# Calculate the sample mean and standard deviation.
# Assume that all conditions necessary for inference are satisfied.
# Use the t-distribution in any calculations.


from scipy.stats import t
import numpy as np

# 单总体均值区间估计P144->反用


class Solution():

    @staticmethod
    def solve():
        lower = 18.985
        higher = 21.015
        mean = (lower + higher) / 2
        alpha = 0.05
        n = 36
        var = (higher - mean) * (np.sqrt(n) / t.ppf(1 - alpha / 2, n - 1))
        return [round(mean, 2), round(var, 2)]

if __name__ == '__main__':
    S = Solution()
    print(S.solve())
