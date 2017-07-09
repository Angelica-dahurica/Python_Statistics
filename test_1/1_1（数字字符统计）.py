# -*- coding:utf-8 -*-
# 已知有一个由数字字符串构成的列表，统计列表中数字字符'0'-'9'各自出现的次数并返回统计结果


class Solution:
    @staticmethod
    def solve(a):
        # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是self。

        diction = {}.fromkeys(range(0,10),0)
        # fromkeys()函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
        # dict.fromkeys(seq[, value]))

        for s in a:
            for item in range(0,len(s)):
                diction[int(s[item:item+1])] += 1
        return diction

if __name__ == '__main__':
    solution = Solution()
    arr = ['12', '34', '567', '36', '809', '120']
    print solution.solve(arr)