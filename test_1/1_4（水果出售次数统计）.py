# -*- coding:utf-8 -*-
# 已知列表fruits中顺序保存了某商店每日出售的水果品名，
# 例如fruits=['apple','banana','cherry','pineapple','banana','peach','pear','peach','cherry' ]，
# 完成函数solve()计算每一种水果的出售次数，存入字典result中并将结果返回


class Solution():
    def solve(self, A):
        dict = {}.fromkeys(A,0)
        for str in A:
            dict[str] += 1
        return dict

solution = Solution()
list=['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear','peach', 'cherry' ]
print(solution.solve(list))
