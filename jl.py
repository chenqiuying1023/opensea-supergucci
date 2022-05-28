from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib as mpl

# iOS系统
# mpl.use('TkAgg')
import matplotlib.pyplot as plt
# from sklearn.preprocessing import Imputer  # 导入sklearn.preprocessing中的Imputer库

# 聚类数据
def KK(ind , path):
    df1 = pd.read_csv(path, header=None, encoding='utf-8', sep=',')
    # df1 = df1.T
    # df1 = df1.drop(df1.index[0], axis=0)
    # df1 = df1.T
    print(df1)
    df1 = (df1 - df1.min()) / (df1.max() - df1.min() + 0.00000000000000000000000001)
    df1 = df1.fillna(df1.mean())  # 用平均数代替,选择各自列的均值替换缺失值


    kmeans = KMeans(n_clusters=ind,init="k-means++",
        n_init=10,
        max_iter=300,
        tol=1e-4,
        verbose=0,
        random_state=None,
        copy_x=True,
        algorithm="auto").fit(df1)
    df1['jllable'] = kmeans.labels_
    df_count_type = df1.groupby('jllable').apply(np.size)


    ##新的dataframe，命名为new_df ，并输出到本地，命名为new_df.csv。
    new_df = df1[:]
    new_df.to_csv('f/new_df'+ str(ind)+'.csv')

    ##将用于聚类的数据的特征的维度降至2维，并输出降维后的数据，形成一个dataframe名字new_pca
    pca = PCA(n_components=2)
    new_pca = pd.DataFrame(pca.fit_transform(new_df))

    ##可视化
    # d = new_pca[new_df['jllable'] == 0]
    # plt.plot(d[0], d[1], 'r.')
    # d = new_pca[new_df['jllable'] == 1]
    # plt.plot(d[0], d[1], 'go')
    # d = new_pca[new_df['jllable'] == 2]
    # plt.plot(d[0], d[1], 'b*')
    # d = new_pca[new_df['jllable'] == 3]
    # plt.plot(d[0], d[1], 'y+')
    # plt.gcf().savefig('kmean'+ str(ind)+'.png')
    # plt.show()
    return kmeans.inertia_

arr = []
for i in range(1,20):
    arr.append(KK(i , './csv/dkr1.csv'))


plt.plot(range(1,20), arr)
plt.gcf().savefig('png/kmean-n1.png')
plt.show()


arr = []
for i in range(1,20):
    arr.append(KK(i , './csv/dkr2.csv'))


plt.plot(range(1,20), arr)
plt.gcf().savefig('png/kmean-n2.png')
plt.show()