# -*- coding:utf-8 -*-
# 完成函数solve，判断传入的整数列表A中的数字是否是素数，并将所有的素数保存到另一个列表中并返回


class Solution():
    def solve(self, A):
        result = []
        index = 0
        for i in A:
            if (self.isPrime(i)):
                result.insert(index, i)
                index += 1
        return result

    # judge whether x is prime or not
    def isPrime(self, x):
        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    return False
            else:
                return True
        else:
            return False

solution = Solution()
list=[23,45,76,67,17]
print(solution.solve(list))