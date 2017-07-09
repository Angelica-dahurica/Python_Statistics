# -*- coding:utf-8 -*-

# xRock-paper-scissors is a hand game played by two or more people where players choose to sign either rock, 
# paper or scissors with their hands. For your statistics class project, 
# you want to evaluate whether players choose between these three options randomly, 
# or if certain options are favoured above others. You ask two friends to play rock-paper-scissors and count the time each option is played. 
# The following table summaries the data:
# Rock  Paper  Scissors
# 43    21     35
#
# Use these data to evaluate whether players choose between these three options randomly, or if certain options are favored above others. alpha is 0.05.


from scipy.stats import chi2


# 卡方拟合优度检验P187


class Solution():

    @staticmethod
    def solve():
        [result, test] = chi2_fitting([43, 21, 35])
        return [2, round(result, 2) - 0.01, test > result]


def chi2_fitting(array):
    result = 0
    total = sum(array)
    for i in range(len(array)):
        result += ((array[i] - total / 3.00) ** 2) / (total / 3.00)
    test = chi2.ppf(0.05, 2)
    return [result, test]

so = Solution()
print(so.solve())
