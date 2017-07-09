# -*- coding:utf-8 -*-

# New York is known as "the city that never sleeps". A random sample of 25 New Yorkers were asked how much sleep they get per night. 
# Statistical summaries of these data are shown below. 
# Do these data provide strong evidence that New Yorkers sleep less than 8 hours per night on average?
# Null-hypothesis is H0: u=8, and alpha is 0.05
# n   mean   stand-variance   min   max
# 25  7.73   0.77             6.17  9.78
#
# Extra:
# (1) If you were to construct a 90% confidence interval that corresponded to this hypothesis test, 
# would you expect 8 hours to be in the interval? Explain your reasoning.


import numpy as np
from scipy.stats import t


# 单总体均值的检验P169


class Solution():

    @staticmethod
    def solve():
        u = 8
        alpha = 0.05
        n = 25
        mean = 7.73
        var = 0.77
        result = (mean - u) / (var / np.sqrt(n))
        test = t.ppf(alpha, n - 1)
        return [n - 1, round(result, 2), (result > test)]

if __name__ == '__main__':
    S = Solution()
    print(S.solve())
