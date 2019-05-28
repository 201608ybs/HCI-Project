# -*- coding: UTF-8 -
import AP
from DataGenerator import generate_cluster_data, generate_random_data

a = [0.00, 0.00]


def read_data(filename):
    result = []
    f = open(filename)
    line = f.readline()
    first_data_str = line.split(" ")
    first_data = [float(x) for x in first_data_str]
    current_time = first_data[0]
    sequence = []
    while line != "":
        temp = line.split(" ")
        data = [float(x) for x in temp]
        if data[0] - current_time < 0.02:
            sequence.append(data[1:])
            current_time = data[0]
        else:
            result.append(sequence)
            sequence = []
            sequence.append(data[1:])
            current_time = data[0]
        line = f.readline()
    result.append(sequence)
    return result


if __name__ == "__main__":
    # sequences = read_data("./testData2.txt")
    sequence_per_cluster = 30
    factor = 10
    print("Test begin:")
    for i in range(0, 5):
        filename = "./clusterData%d.txt" % (i + 1)
        # generate_cluster_data((i + 1) * sequence_per_cluster, a, filename)
        sequences = read_data(filename)
        length = len(sequences)
        A = AP.init_matrix_a(length)
        R = AP.init_matrix_r(length)
        seq_distance_list = AP.cal_seq_list(sequences)
        cluster_centers = AP.cal_cluster_centers(length, seq_distance_list, R, A)
        print("Test data cluster num: %d Sequence per cluster: %d Cluster num after calculation: %d" % (
            i + 1, sequence_per_cluster, len(cluster_centers)))
        # clusters = AP.cal_clusters(cluster_centers, sequences)
