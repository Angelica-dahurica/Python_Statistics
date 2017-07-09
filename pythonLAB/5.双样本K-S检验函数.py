#-*- coding:utf-8 -*-
'''
描述：
利用python实现简化版双样本K-S检验函数
输入：
a,b分别为非空一维数组；示例输入 : [1.0,2.0,3.0],[1.0,2.0,3.0]
输出：
ks-value为检验结果KS值；示例输出 : 0.0
注意：
（1）不能调用math、scipy、numpy包
'''
#公式参考教材第196页
class Solution():
    def ks_2samp(self, data1, data2):
        size1=len(data1)
        size2=len(data2)
        data=[]

        for i in data1:
            data.append(float(i))
        for i in data2:
            data.append(float(i))

        data=list(set(data))
        data.sort()

        p1=[]
        p2=[]
        for i in data:
            count1=0
            count2=0
            for j in data1:
                if(float(j)==i):
                    count1+=1
            p1.append(count1)
            for k in data2:
                if (float(k)==i):
                    count2+=1
            p2.append(count2)
        
        sum1=0
        sum2=0
        dirta=[]
        for i in range(len(data)):
            sum1+=float(p1[i])
            f=sum1/size1
            sum2+=float(p2[i])
            g=sum2/size2
            d=abs(f-g)
            dirta.append(d)

        return max(dirta)
a=Solution()
data2=[73, 57, 0, 99, 42, 19]
data1=[45, 15, 38, 41, 51, 82]
print(a.ks_2samp(data1, data2))
