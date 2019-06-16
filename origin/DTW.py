# -*- coding: UTF-8 -

import numpy as np
import math


def cal_distance(point1, point2, type):
    distance = 0
    if type == 0:  # 计算方向的差异
        vec1 = np.array(point1)
        vec1 = vec1 / np.sqrt(np.sum(np.square(vec1)))
        vec2 = np.array(point2)
        vec2 = vec2 / np.sqrt(np.sum(np.square(vec2)))
        vec3 = vec1 * vec2
        dot_result = np.sum(vec3)
        if dot_result > 1.0:
            dot_result = 1.0
        distance = math.acos(dot_result) * 180 / math.pi / 180
    elif type == 1:  # 计算Yaw角差异
        if abs(point1 - point2) > 180:
            distance = (360 - abs(point1 - point2)) / 180
        else:
            distance = abs(point1 - point2) / 180
    elif type == 2:  # 计算弯曲度差异
        distance = abs(point1 - point2) / 200
    return distance
    # if type(point1) == list:
    #     vec1 = np.array(point1)
    #     vec1 = vec1 / np.sqrt(np.sum(np.square(vec1)))
    #     vec2 = np.array(point2)
    #     vec2 = vec2 / np.sqrt(np.sum(np.square(vec2)))
    #     vec3 = vec1 * vec2
    #     distance = math.acos(np.sum(vec3)) * 180 / math.pi
    # else:
    #     if abs(point1 - point2) > 180:
    #         distance = 360 - abs(point1 - point2)
    #     else:
    #         distance = abs(point1 - point2)
    # return distance


def DTW(sequence1, sequence2, type):
    r, c = len(sequence1), len(sequence2)
    # 添加一行和一列便于动态规划
    D0 = np.zeros((r + 1, c + 1))
    D0[0, 1:] = np.inf
    D0[1:, 0] = np.inf
    # 浅拷贝
    D1 = D0[1:, 1:]

    for i in range(r):
        for j in range(c):
            D1[i, j] = cal_distance(sequence1[i], sequence2[j], type)

    # 深拷贝，保存起始距离信息
    M = D1.copy()

    for i in range(r):
        for j in range(c):
            D1[i, j] += min(D0[i, j], D0[i, j + 1], D0[i + 1, j])

    # 计算最短路径
    i, j = np.array(D0.shape) - 2
    count = 1
    while i > 0 or j > 0:
        tb = np.argmin((D0[i, j], D0[i, j + 1], D0[i + 1, j]))
        if tb == 0:
            i -= 1
            j -= 1
        elif tb == 1:
            i -= 1
        else:
            j -= 1
        count = count + 1
    return D1[-1, -1] / count


def get_sequence_set(filename):
    """
    将采集到手势的时间序列进行拆分，得到该手势姿态角的时间序列，Yaw角的时间序列，弯曲度的时间序列
    :param filename:存储手势数据的文件名
    :return: 姿态角的时间序列，Yaw角的时间序列，弯曲度的时间序列
    """
    f1 = open(filename, 'r')
    fingers_direction = [[], [], [], [], []]
    fingers_spin = [[], [], [], [], []]
    fingers_roll = [[], [], [], [], []]
    for line in f1:
        temp = line.split(",", -1)
        for i in range(0, 5):
            x = float(temp[3 * i + 1]) * math.pi / 180
            y = float(temp[3 * i + 2]) * math.pi / 180
            z = float(temp[3 * i + 3])
            point = [math.cos(x) * math.cos(y), math.sin(x) * math.cos(y), math.sin(y)]
            fingers_direction[i].append(point)
            fingers_spin[i].append(z)
            fingers_roll[i].append(float(temp[16 + i]))
    return fingers_direction, fingers_spin, fingers_roll  # 依次表示姿态角，Yaw角，弯曲度的sequence


def cal_sequence_dist(filename1, filename2):
    sequence_set_1 = get_sequence_set(filename1)
    sequence_set_2 = get_sequence_set(filename2)
    total = 0.0
    for i in range(0, 5):
        direction_sequence_dist = DTW(sequence_set_1[0][i], sequence_set_2[0][i], 0)
        yaw_sequence_dist = DTW(sequence_set_1[1][i], sequence_set_2[1][i], 1)
        # 两手势弯曲度之间的距离 curvature:弯曲度
        curvature_sequence_dist = DTW(sequence_set_1[2][i], sequence_set_2[2][i], 2)
        total += 0.6 * direction_sequence_dist + 0.1 * yaw_sequence_dist + 0.3 * curvature_sequence_dist
    return total


if __name__ == "__main__":
    print(cal_sequence_dist("./data/data1-3.txt", "./data/hou-data4-3.txt"))
