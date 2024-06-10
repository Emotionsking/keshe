import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#设置字体与负号显示
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus'] = False
#读取Excel数据
data=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/酿酒行业2022.xlsx')
#获取列名与数据值
name = data.columns.values
values=data.values
#创建图像与子图
p = plt.figure(figsize=(10,10))
ax1 = p.add_subplot(2,1,1)
#选择标签和数据值
label1 =values[range(0,values[:,1].size,1),1]
gdp1 = list(values[range(0,values[:,1].size,1),2:6])
#绘制箱线图
plt.boxplot(gdp1,notch=True,tick_labels = label1, meanline=True)
#设置x轴刻度
xticks = range(1, len(label1)+1)
plt.xticks(xticks, label1, rotation=45)
#绘制线图
plt.plot(xticks, values[range(0,values[:,3].size,1),3],'b-')
#设置布局与标题
plt.title("2022年酿酒行业k线走势")
plt.ylabel("每股单价(元)")
plt.xlabel('时间')
plt.tight_layout()
#%%
#读取Excel数据
data=pd.read_excel('C:/Users/28711/Desktop/股票分析/行业k线数据(周)/酿酒行业2023.xlsx')
#获取列名与数据值
name = data.columns.values
values=data.values
#创建图像与子图
p = plt.figure(figsize=(10,10))
ax1 = p.add_subplot(2,1,1)
#选择标签和数据值
label1 =values[range(0,values[:,1].size,1),1]
gdp1 = list(values[range(0,values[:,1].size,1),2:6])
#绘制箱线图
plt.boxplot(gdp1,notch=True,tick_labels = label1, meanline=True)
#设置x轴刻度
xticks = range(1, len(label1)+1)
plt.xticks(xticks, label1, rotation=45)
#绘制线图
plt.plot(xticks, values[range(0,values[:,3].size,1),3],'b-')
#设置布局与标题
plt.title("2023年酿酒行业k线走势")
plt.ylabel("每股单价(元)")
plt.xlabel('时间')
plt.tight_layout()
plt.show()