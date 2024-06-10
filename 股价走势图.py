import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus'] = False
data1=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/酿酒行业2022.xlsx')
name1=data1.columns.values
values1=data1.values
data2=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/酿酒行业2023.xlsx')
name2=data2.columns.values
values2=data2.values
data3=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/半导体2022.xlsx')
name3=data3.columns.values
values3=data3.values
data4=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/半导体2023.xlsx')
name4=data4.columns.values
values4=data4.values
data5=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/电子元件2022.xlsx')
name5=data5.columns.values
values5=data5.values
data6=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/电子元件2023.xlsx')
name6=data6.columns.values
values6=data6.values
data7=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/玻璃纤维2022.xlsx')
name7=data7.columns.values
values7=data7.values
data8=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/玻璃纤维2023.xlsx')
name8=data8.columns.values
values8=data8.values
data9=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/纺织服装2022.xlsx')
name9=data9.columns.values
values9=data9.values
data10=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/纺织服装2023.xlsx')
name10=data10.columns.values
values10=data10.values
label2 = ["酿酒行业", "半导体", "电子元件", "玻璃纤维", "纺织服装"]
p = plt.figure(figsize=(30, 14))
ax3 = p.add_subplot(3, 2, 1)
y1 = [values1[:, 3][0], values3[:, 3][0], values5[:, 3][0], values7[:, 3][0], values9[:, 3][0]]
y2 = [values2[:, 3][0], values4[:, 3][0], values6[:, 3][0], values8[:, 3][0], values10[:, 3][0]]
x = [1, 2, 3, 4, 5]
plt.xticks(x, label2)
plt.bar([0.8, 1.8, 2.8, 3.8, 4.8], y1, width=0.4)
plt.bar([1.2, 2.2, 3.2, 4.2, 5.2], y2, width=0.4)
plt.legend(['2022', '2023'])
plt.xlabel('行业')
plt.ylabel('每股单价(元)')
plt.title('2022年与2023年年初各行业股价直方图')
p = plt.figure(figsize=(12,12))
ax1 = p.add_subplot(2,1,1)
label1 =values1[range(0,values1[:,1].size,1),1]
label2 =values2[range(0,values2[:,1].size,1),1]
xticks1 = range(1, len(label1)+1)
xticks = range(1, len(label2)+1)
plt.xticks(xticks1, label1, rotation=45)
plt.plot(
    xticks1, values1[range(0,values1[:,3].size,1),3],'b',
         xticks1, values3[range(0,values3[:,3].size,1),3],'r',
         xticks1, values5[range(0,values5[:,3].size,1),3],'y',
         xticks1, values7[range(0,values7[:,3].size,1),3],'c',
         xticks1, values9[range(0,values9[:,3].size,1),3],'g',
         xticks, values2[range(0, values2[:, 3].size, 1), 3], 'b--',
         xticks, values4[range(0, values4[:, 3].size, 1), 3], 'r--',
         xticks, values6[range(0, values6[:, 3].size, 1), 3], 'y--',
         xticks, values8[range(0, values8[:, 3].size, 1), 3], 'c--',
         xticks, values10[range(0, values10[:, 3].size, 1), 3], 'g--',
        )
plt.legend(["酿酒行业", "半导体", "电子元件","玻璃纤维", "纺织服装",])
plt.title("2022年与2023年行业股价走势折线图")
plt.ylabel("每股单价(元)")
plt.xlabel('时间')
plt.show()
#读取数据
data=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/电子元件2022.xlsx')
#对数据进行聚合和分类统计
rise=len(data[data['涨跌幅']>=0])
fall=len(data[data['涨跌幅']<0])
total=len(data)
#绘制饼状图
labels = ['上涨','下跌']
sizes = [rise/total, fall/total]
colors = ['yellow','blue']
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', startangle=90)
plt.title('2022年电子元件涨跌对比')
plt.show()
print(rise,fall,total)
#读取数据
data=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/电子元件2023.xlsx')
#对数据进行聚合和分类统计
rise=len(data[data['涨跌幅']>=0])
fall=len(data[data['涨跌幅']<0])
total=len(data)
#绘制饼状图
labels = ['上涨','下跌']
sizes = [rise/total, fall/total]
colors = ['yellow','blue']
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', startangle=90)
plt.title('2023年电子元件涨跌对比')
print(rise,fall,total)
plt.show()