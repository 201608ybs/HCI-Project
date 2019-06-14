# -*- coding: UTF-8 -
import numpy as np


def cal_distance(point1, point2):
    vec1 = np.array(point1)
    vec2 = np.array(point2)

    distance = np.sqrt(np.sum(np.square(vec1 - vec2)))
    return distance


def DTW(sequence1, sequence2, path):
    r, c = len(sequence1), len(sequence2)
    # 添加一行和一列便于动态规划
    D0 = np.zeros((r + 1, c + 1))
    D0[0, 1:] = np.inf
    D0[1:, 0] = np.inf
    # 浅拷贝
    D1 = D0[1:, 1:]

    for i in range(r):
        for j in range(c):
            D1[i, j] = cal_distance(sequence1[i], sequence2[j])

    # 深拷贝，保存起始距离信息
    M = D1.copy()

    for i in range(r):
        for j in range(c):
            D1[i, j] += min(D0[i, j], D0[i, j + 1], D0[i + 1, j])

    # 计算最短路径
    i, j = np.array(D0.shape) - 2
    p, q = [i], [j]
    while i > 0 or j > 0:
        tb = np.argmin((D0[i, j], D0[i, j + 1], D0[i + 1, j]))
        if tb == 0:
            i -= 1
            j -= 1
        elif tb == 1:
            i -= 1
        else:
            j -= 1
        p.insert(0, i)
        q.insert(0, j)
    path = zip(p, q)
    return D1[-1, -1]
