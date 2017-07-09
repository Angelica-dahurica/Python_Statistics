#coding: utf-8
import random

'''
n表示赢钱需要的局数
n1表示第一个人已经赢的局数
n2表示第二个人已经赢的局数

程序模拟赌徒继续下去，返回最终赢的那个人的编号（1或者2）
'''
def Bookie(n,n1,n2):
    for i in range(2*n-n1-n2-1):
        D=random.randint(1,2)
        if D==1:
            n1+=1
        else:
            n2+=1
        if n1==n:
            return 1
        if n2==n:
            return 2

if __name__ == '__main__':  
    n=10000
    win=0
    for i in range(n):
        if(Bookie(10,5,2)==1):
            win+=1
    print (float(win)/n)
    print (1-float(win)/n)
