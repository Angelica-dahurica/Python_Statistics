# -*- coding:utf-8 -*-
# 对于一个包含一系列数字字符串的列表，寻找其中的回文串存入一个列表中并返回


class Solution():
    def solve(self, A):
        # [] 表示列表
        result = []
        x = 0
        for i in A:
            if(self.is_palindrome(i)):
                # list.insert(index, obj)
                result.insert(x, i)
                x += 1
        return result

    # use isPalindrom function to check if the string is palindrome or not
    @staticmethod
    def is_palindrome(self, x):
        for item in range(0,len(x)):
            if(x[item:item+1] == x[len(x)-item-1:len(x)-item]):
                continue
            else:
                return False
        return True

solution = Solution()
list=['123', '232', '4556554', '12123', '3443','1314131']
print(solution.solve(list))
