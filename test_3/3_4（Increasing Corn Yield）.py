# -*- coding:utf-8 -*-

# A large farm wants to try out a new type of fertilizer to evaluate whether it will improve the farm's corn production. 
# The land is broken into plots that produce an average of 1.215 pounds of corn with a standard deviation of 94 pounds per plot. 
# The owner is interested in detecting any average difference of at least 40 pounds per plot. 
# How many plots of land would be needed for the experiment if the desired power level is 90%? 
# Assume each plot of land gets treated with either the current fertilizer or the new fertilizer.


import numpy as np
from scipy.stats import norm

class Solution:

    @staticmethod
    def solve():
        var = 94
        n = 1
        mu = 40
        while mu / np.sqrt(2 * var**2 / n) < (norm.ppf(0.9) + norm.ppf(0.975)):
            n += 1
        return n

if __name__ == '__main__':
    S = Solution()
    print(S.solve())
