import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
df=pd.read_excel('C:/Users/28711/Desktop/股票分析/数据处理(年)/年总数据1.xlsx')
# 关注两个指标：涨跌幅和振幅
data = df[['涨跌幅(%)', '振幅(%)']]
original_data_df = df[['涨跌幅(%)', '振幅(%)']]
# 对数据进行标准化处理
scaler = StandardScaler()
data = scaler.fit_transform(data)
#使用肘部图确定最佳的簇数量
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots(figsize=(22, 10))
ax.set_facecolor('#F1F3F9')  # 设置背景颜色
ax.grid(True, linestyle='--', linewidth=0.5, color='gray')  # 添加网格
plt.plot(range(1, 11), wcss)
plt.title('肘部图')
plt.xlabel('簇的数量')
plt.ylabel('WCSS')
plt.show()
# 使用K-means聚类算法将数据分为4个簇
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(data)
# 创建一个新的DataFrame，包含'股票简称'、'日期'和聚类结果
result_df = pd.DataFrame({
    '股票简称': df['股票简称'],
    '日期': df['日期'],
    '聚类结果': pred_y,
    '涨跌幅(%)_原始': original_data_df['涨跌幅(%)'],
    '振幅(%)_原始': original_data_df['振幅(%)']
})
# 将标准化后的数据转换为DataFrame
standardized_data_df = pd.DataFrame(data, columns=['涨跌幅(%)_标准化', '振幅(%)_标准化'])
# 将标准化后的数据合并到result_df中
result_df = pd.concat([result_df, standardized_data_df], axis=1)
# 按照聚类结果进行排序
result_df = result_df.sort_values(by='聚类结果', ascending=True)
# 将DataFrame保存到Excel文件
result_df.to_excel('聚类结果.xlsx', index=False)
# 可视化聚类结果
fig, ax = plt.subplots(figsize=(22, 10))
ax.set_facecolor('#F1F3F9')  # 设置背景颜色
ax.grid(True, linestyle='--', linewidth=0.5, color='gray')  # 添加网格
plt.scatter(data[:,0], data[:,1], c=pred_y, cmap='viridis')
plt.colorbar()
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='*', s=200, alpha=0.9)
plt.xlabel('涨跌幅(%)')
plt.ylabel('振幅(%)')
plt.title('股票聚类分析结果')
plt.show()
# 分析每个簇的特征
df['cluster'] = pred_y
for i in range(4):
    print('Cluster ' + str(i) + ':')
    print(df[df['cluster']==i][['涨跌幅(%)', '振幅(%)']].describe())