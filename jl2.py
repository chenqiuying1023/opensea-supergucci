from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib as mpl

# iOS系统
# mpl.use('TkAgg')
import matplotlib.pyplot as plt
# from sklearn.preprocessing import Imputer  # 导入sklearn.preprocessing中的Imputer库
def toint(b):
    return b
    print("---------------------")
    print("---------------------")
    print(b)
    arr =[]
    for i in b:
        if i:
            arr.append( 1)
        else:
            arr.append(0)
    return arr

# 聚类数据
def KK(ind , path ,savePath):
    df1 = pd.read_csv(path, header=None, encoding='utf-8', sep=',')
    # df1 = df1.T
    # df1 = df1.drop(df1.index[0], axis=0)
    # df1 = df1.T
    df1=(df1 - df1.min()) / (df1.max() - df1.min() + 0.0000000000000000001)
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

    ##各个类别的数目
    print(df_count_type)
    #聚类中心
    # print(kmeans.cluster_centers_)
    # kmeans.inertia_

    ##新的dataframe，命名为new_df ，并输出到本地，命名为new_df.csv。
    new_df = df1[:]
    new_df.to_csv('file/'+ savePath+ str(ind)+'.csv')
    ##将用于聚类的数据的特征的维度降至2维，并输出降维后的数据，形成一个dataframe名字new_pca
    pca = PCA(n_components=2)
    new_pca = pd.DataFrame(pca.fit_transform(new_df))


    ##可视化
    d = new_pca[toint(new_df['jllable'] == 0)]
    plt.plot(d[0], d[1], 'r.')
    d = new_pca[toint(new_df['jllable'] == 1)]
    plt.plot(d[0], d[1], 'go')
    d = new_pca[toint(new_df['jllable'] == 2)]
    plt.plot(d[0], d[1], 'b*')
    d = new_pca[toint(new_df['jllable'] == 3)]
    plt.plot(d[0], d[1], 'y+')
    plt.gcf().savefig('png/kmean'+savePath+ str(ind)+'.png')
    plt.show()


    return kmeans.inertia_

arr = []
ind = range(3,5)
for i in ind:
    arr.append(KK(i , './csv/dkr1.csv', "dkr1v"))

#
# plt.plot(ind, arr)
# plt.gcf().savefig('png/kmean-n1.png')
# plt.show()


arr = []
for i in ind:
    arr.append(KK(i , './csv/dkr2.csv' , "dkr2v"))



# plt.plot(ind, arr)
# plt.gcf().savefig('png/kmean-n2.png')
# plt.show()
