# -*- coding:utf-8 -*-
# 下面为利用蒙特卡罗方法计算π的python实现代码，请仔细阅读，理解代码含义，并试着写出你自己版本的计算π的蒙特卡罗方法

import random
'''
You can delete the MontyCarlo and write your Monty Carlo
'''

# this function may spend a little time to execute

# 当所求解问题是某种随机事件出现的概率，或者是某个随机变量的期望值时，通过某种“实验”的方法，
# 以这种事件出现的频率估计这一随机事件的概率，或者得到这个随机变量的某些数字特征，并将其作为问题的解。


def montycarlo():  # 使用几何方法
    n = 1000000
    k = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            k += 1
    return 4 * float(k) / float(n)

if __name__ == '__main__':
    pi = montycarlo()
    # print out the result
    print(pi)
