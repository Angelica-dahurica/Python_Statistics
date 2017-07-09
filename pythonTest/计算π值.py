import random
import math

'''
通过蒲丰投针问题来计算π值
若干条相互平行、相距为d的直线布满整个空间，在平面上随机投下一根长为l的针(l<d)
定义针与直线所夹锐角为x,针的中点离它最近的直线的距离为y
因为l<d，所以针最多有一个交点
定义域：0<y<d/2,0<x<π/2
针落在直线上的概率p=(2*l)/(π*d)
'''

#this function may spend a little time to execute
def MontyCarlo():
    n = 1000000
    k = 0
    
    d=random.randint(0,n)
    l=random.randint(0,d)
    for i in range(n):
        x = random.uniform(0,math.pi/2)
        y = random.uniform(0, d/2)
        if y<=(l/2)*math.sin(x):
            k = k + 1
    return 2*l /( d*float(k) / float(n) )

if __name__ == '__main__':  
    print (MontyCarlo())
