# -*- coding: UTF-8 -
import random
import math


def generate_cluster_dir(cluster_num, sequence_per_cluster, factor):
    directions = []
    for i in range(cluster_num):
        # 生成每一簇数据中心点陀螺仪数据
        base_direction = [random.random(), random.random(), random.random()]
        for j in range(0, sequence_per_cluster):
            # 对数据进行微调
            x = base_direction[0] + random.uniform(-base_direction[0] / factor, base_direction[0] / factor)
            y = base_direction[1] + random.uniform(-base_direction[1] / factor, base_direction[1] / factor)
            z = base_direction[2] + random.uniform(-base_direction[2] / factor, base_direction[2] / factor)
            model = math.sqrt(x * x + y * y + z * z)
            x /= model
            y /= model
            z /= model
            directions.append([x, y, z])
    return directions


def generate_cluster_angle(cluster_num, sequence_per_cluster, factor):
    angles = []
    for i in range(0, cluster_num):
        # 生成每一簇数据中心点五指弯曲度数据
        base_angle = [random.uniform(0, math.pi / 2), random.uniform(0, math.pi / 2),
                      random.uniform(0 / 2, math.pi / 2), random.uniform(0, math.pi / 2),
                      random.uniform(0 / 2, math.pi / 2)]
        for j in range(0, sequence_per_cluster):
            # 对数据进行微调
            angle1 = base_angle[0] + random.uniform(-base_angle[0] / factor, base_angle[0] / factor)
            angle2 = base_angle[1] + random.uniform(-base_angle[1] / factor, base_angle[1] / factor)
            angle3 = base_angle[2] + random.uniform(-base_angle[2] / factor, base_angle[2] / factor)
            angle4 = base_angle[3] + random.uniform(-base_angle[3] / factor, base_angle[3] / factor)
            angle5 = base_angle[4] + random.uniform(-base_angle[4] / factor, base_angle[4] / factor)
            angles.append([angle1, angle2, angle3, angle4, angle5])
    return angles


def generate_cluster_data(sequence_num, cluster_num, sequence_per_cluster, a, factor, filename):
    directions = generate_cluster_dir(cluster_num, sequence_per_cluster, factor)
    angles = generate_cluster_angle(cluster_num, sequence_per_cluster, factor)
    # 将测试数据写入文件
    write_file(filename, directions, angles, sequence_num, a)


def generate_random_dir(sequence_num):
    directions = []
    for i in range(sequence_num):
        x = random.random()
        y = random.random()
        z = random.random()
        model = math.sqrt(x * x + y * y + z * z)
        x /= model
        y /= model
        z /= model
        directions.append([x, y, z])
    return directions


def generate_random_angle(sequence_num):
    angles = []
    for i in range(0, sequence_num):
        angle1 = random.uniform(0, math.pi / 2)
        angle2 = random.uniform(0, math.pi / 2)
        angle3 = random.uniform(0, math.pi / 2)
        angle4 = random.uniform(0, math.pi / 2)
        angle5 = random.uniform(0, math.pi / 2)
        angles.append([angle1, angle2, angle3, angle4, angle5])
    return angles


def generate_random_data(sequence_num, a, filename):
    directions = generate_random_dir(sequence_num)
    angles = generate_random_angle(sequence_num)
    write_file(filename, directions, angles, sequence_num, a)


def write_file(filename, directions, angles, sequence_num, a):
    f = open(filename, 'w')
    for i in range(0, sequence_num):
        for j in range(1, 6):
            line = str(i + 0.01 * j)
            for k in directions[i]:
                line = line + " " + "%.6f" % k
            for k in angles[i]:
                line = line + " " + "%.6f" % k
            for k in a:
                line = line + " " + str(k)
            f.write(line + "\n")
    f.close()
