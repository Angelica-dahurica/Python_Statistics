#-*- coding:utf-8 -*-
'''
美国疾病控制与预防中心（CDC）从1973年开始推行全国家庭成长调查（NSFG），目的是收集（美国）
“家庭的生活、婚姻状况、生育、避孕和男女健康信息。”
现有从2002年1月到3月收集的调查数据（url为http://112.124.1.3:8050/getData/101），
包含上万条调查数据
另据某研究显示，婴儿出生周数符合方差为16的正态分布，
试写函数solve估计婴儿平均出生周数的置信区间（置信水平为95%）。
输入：
调查样本数据，格式为{“status”:"ok","data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}
每条数据包括
01 caseid（标识符）,
2  prglength（婴儿第几周出生）,
3  outcome（怀孕结果，1表示活产）,
4 totalwgt_oz（婴儿出生重量，单位盎司）,
5 birthord（第几胎,1表示第一胎）,
6 agepreg（怀孕时年龄）,
7 finalwgt（被调查者的统计权重，表明这名调查者所代表的人群在美国总人口中的比例。）

输出：

[lower,upper]分别代表平均出生周数的估计下限与上限

注意：

（1）婴儿第几周出生数据由于被调查人选填错误等原因出现了一些不合理数据，
比如错填了月份（5<prglength<=10），
其他错填（prglength<=5, 10<prglength<=25, prglength>=49），
对于错填月份的情况，将月份*4.33作为其周数，对于其他错填情况则舍弃此条数据
'''

#爬数据的方法
'''
import urllib2
response = urllib2.urlopen('http://112.124.1.3:8050/getData/101')  
html = response.read()
'''
#公式参见144页

import urllib2 
class Solution():
    def solve(self):
#        response = urllib2.urlopen('http://112.124.1.3:8050/getData/101')  
#        html = response.read()

        html='{“status”:"ok","data":[[1, 1, 38, 1, 141, 1,33.16,6448.271111704751],[1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751],[31, 1, 42, 1, 114, 1, 18.83, 5211.9431128540555]]}'        
        data=html.split('[[')[1].split(']}')[0].split(',')
        size=len(data)

        mon=[]
        for i in range(size/8):
            prglength=float(data[i*8+2])
            if(prglength>5 and prglength<=10):
                prglength=prglength*4.33
            elif(prglength<=5 or (prglength>10 and prglength<=25) or prglength>=49):
                continue
            mon.append(prglength)

        n=len(mon)
        sum=0
        for i in mon:
            sum+=i
        mean=sum/n
        z=1.96
        tem=4/float(n**0.5)
        lower=mean-tem*z
        upper=mean+tem*z
        return [lower,upper]
        
A=Solution()
print(A.solve())
