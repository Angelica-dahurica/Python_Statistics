# -*- coding:utf-8 -*-

# A group of researchers are interested in the possible effects of distracting stimuli during eating, 
# such as an increase or decrease in the amount of food consumption. 
# To test this hypothesis, they monitored food intake for a group of 44 patients who were randomised into two equal groups. 
# The treatment group ate lunch while playing solitaire, and the control group ate lunch without any added distractions. 
# Patients in the treatment group ate 52.1 grams of biscuits, with a standard deviation of 45.1 grams, 
# and patients in the control group ate 27.1 grams of biscuits with a standard deviation of 26.4 grams. 
# Do these data provide convincing evidence that the average food intake is different for the patients in the treatment group? 
# Assume the conditions for inference are satisfied.
# Null hypothesis is H0: u_t - u_c = 0, alpha is 0.05


from scipy.stats import t as T
import numpy as np


# 双正态总体均值的检验P170


class Solution():

    @staticmethod
    def solve():
        mean1, mean2 = 52.1, 27.1
        u = 0
        var1, var2 = 45.1, 26.4
        n1, n2 = 22, 22
        rv = T(n1 + n2 - 2)
        t = (mean1 - mean2 - u) / np.sqrt((((n1 - 1) * (var1 ** 2) + (n2 - 1) * (var2 ** 2)) / (n1 + n2 - 2) * (1.0 / n1 + 1.0 / n2)))
        test = rv.ppf(0.975)
        return [n1 - 1, round(t, 2), (np.abs(t) < test)]

if __name__ == '__main__':
    S = Solution()
    print(S.solve())
