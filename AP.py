# -*- coding: UTF-8 -
import numpy as np
from DTW import DTW


def cal_seq_list(sequences):
    seq_distance_list = []
    for s in sequences:
        path = []
        temp = []
        for n in sequences:
            seq_distance = DTW(s, n, path)
            temp.append(-seq_distance)
        seq_distance_list.append(temp)

    p = np.median(seq_distance_list)
    for i in range(len(sequences)):
        seq_distance_list[i][i] = p
    return seq_distance_list


def init_matrix_r(length):
    R = [[0] * length for j in range(length)]
    return R


def init_matrix_a(length):
    A = [[0] * length for j in range(length)]
    return A


def iter_update_r(length, R, A, seq_distance_list):
    old_r = 0
    lam = 0.5  # 阻尼系数,用于算法收敛
    # 此循环更新R矩阵
    for i in range(length):
        for k in range(length):
            old_r = R[i][k]
            if i != k:
                max1 = A[i][0] + R[i][0]
                for j in range(length):
                    if j != k:
                        if A[i][j] + R[i][j] > max1:
                            max1 = A[i][j] + R[i][j]
                # 更新后的R[i][k]值
                R[i][k] = seq_distance_list[i][k] - max1
                # 带入阻尼系数重新更新
                R[i][k] = (1 - lam) * R[i][k] + lam * old_r
            else:
                max2 = seq_distance_list[i][0]
                for j in range(length):
                    if j != k:
                        if seq_distance_list[i][j] > max2:
                            max2 = seq_distance_list[i][j]
                # 更新后的R[i][k]值
                R[i][k] = seq_distance_list[i][k] - max2
                # 带入阻尼系数重新更新
                R[i][k] = (1 - lam) * R[i][k] + lam * old_r
    return R


def iter_update_a(length, R, A):
    old_a = 0
    lam = 0.5  # 阻尼系数,用于算法收敛
    # 此循环更新A矩阵
    for i in range(length):
        for k in range(length):
            old_a = A[i][k]
            if i == k:
                max3 = 0
                for j in range(length):
                    if j != k:
                        if R[j][k] > 0:
                            max3 += R[j][k]
                A[i][k] = max3
                # 带入阻尼系数更新A值
                A[i][k] = (1 - lam) * A[i][k] + lam * old_a
            else:
                max4 = 0
                for j in range(length):
                    # 公式中的i!=k 的求和部分
                    if j != k and j != i:
                        if R[j][k] > 0:
                            max4 += R[j][k]

                if R[k][k] + max4 > 0:
                    A[i][k] = 0
                else:
                    A[i][k] = R[k][k] + max4

                # 带入阻尼系数更新A值
                A[i][k] = (1 - lam) * A[i][k] + lam * old_a

    return A


# 计算聚类中心
def cal_cluster_centers(length, seq_distance_list, R, A):
    # 进行聚类，不断迭代直到预设的迭代次数或者判断comp_cnt次后聚类中心不再变化
    max_iter = 100  # 最大迭代次数
    curr_iter = 0  # 当前迭代次数
    max_comp = 30  # 最大比较次数
    curr_comp = 0  # 当前比较次数
    cluster_centers = []  # 聚类中心列表，存储的是数据点在sequences中的索引
    while True:
        # 计算R矩阵
        R = iter_update_r(length, R, A, seq_distance_list)
        # 计算A矩阵
        A = iter_update_a(length, R, A)
        curr_iter += 1
        # 开始计算聚类中心
        for k in range(length):
            if R[k][k] + A[k][k] > 0:
                if k not in cluster_centers:
                    cluster_centers.append(k)
                else:
                    curr_comp += 1
        # print("current iterator times: %d\n" % curr_iter)
        if curr_iter >= max_iter or curr_comp > max_comp:
            break

    return cluster_centers


def cal_clusters(cluster_centers, sequences):
    clusters = []
    for m in sequences:
        temp = []
        for j in cluster_centers:
            n = sequences[j]
            path = []
            d = DTW(m, n, path)
            temp.append(d)
        # 记录聚类中心索引
        c = cluster_centers[temp.index(np.min(temp))]
        clusters.append(c)
    return clusters
