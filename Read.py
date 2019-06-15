import string
import math
from DTW import DTW
import numpy as np

'''
def deal(beforedeal):
    for index in range(len(beforedeal) - 1):
        now = beforedeal[index]
        nex = beforedeal[index + 1]
        if now == nex:
            count = 0
            n = index + 1
            while now == beforedeal[n] and n != len(beforedeal) - 1:
                count = count + 1
                n = n + 1
            for j in range(index, n):
                temp1 = np.array(beforedeal[n])
                temp2 = np.array(now)
                temp3 = np.array(beforedeal[j])
                beforedeal[j] = ((temp1 - temp2) * (j - index) / (n - index) + temp3).tolist()
    return beforedeal
'''

f = open('data1-5.txt', 'r')
fingers_direction = [[], [], [], [], []]
fingers_spin = [[], [], [], [], []]
fingers_roll = [[], [], [], [], []]
for line in f:
    temp = line.split(",", -1)
    for i in range(0, 5):
        x = string.atof(temp[3 * i + 1]) * math.pi / 180
        y = string.atof(temp[3 * i + 2]) * math.pi / 180
        z = string.atof(temp[3 * i + 3])
        point = [math.cos(x) * math.cos(y), math.sin(x) * math.cos(y), math.sin(y)]
        fingers_direction[i].append(point)
        fingers_spin[i].append(z)
        fingers_roll[i].append(string.atof(temp[15 + i]))
finger1_1 = fingers_direction[0]
finger2_1 = fingers_direction[1]
finger3_1 = fingers_direction[2]
finger4_1 = fingers_direction[3]
finger5_1 = fingers_direction[4]
'''
finger1_1 = deal(finger1_1)
finger2_1 = deal(finger2_1)
finger3_1 = deal(finger3_1)
finger4_1 = deal(finger4_1)
finger5_1 = deal(finger5_1)
'''
spin1_1 = fingers_spin[0]
spin2_1 = fingers_spin[1]
spin3_1 = fingers_spin[2]
spin4_1 = fingers_spin[3]
spin5_1 = fingers_spin[4]

roll1_1 = fingers_roll[0]
roll2_1 = fingers_roll[1]
roll3_1 = fingers_roll[2]
roll4_1 = fingers_roll[3]
roll5_1 = fingers_roll[4]

f.close()

f = open('data1-1.txt', 'r')
fingers_direction = [[], [], [], [], []]
fingers_spin = [[], [], [], [], []]
fingers_roll = [[], [], [], [], []]
for line in f:
    temp = line.split(",", -1)
    for i in range(0, 5):
        x = string.atof(temp[3 * i + 1]) * math.pi / 180
        y = string.atof(temp[3 * i + 2]) * math.pi / 180
        z = string.atof(temp[3 * i + 3])
        point = [math.cos(x) * math.cos(y), math.sin(x) * math.cos(y), math.sin(y)]
        fingers_direction[i].append(point)
        fingers_spin[i].append(z)
        fingers_roll[i].append(string.atof(temp[15 + i]))
finger1_2 = fingers_direction[0]
finger2_2 = fingers_direction[1]
finger3_2 = fingers_direction[2]
finger4_2 = fingers_direction[3]
finger5_2 = fingers_direction[4]
'''
finger1_2 = deal(finger1_2)
finger2_2 = deal(finger2_2)
finger3_2 = deal(finger3_2)
finger4_2 = deal(finger4_2)
finger5_2 = deal(finger5_2)
'''
spin1_2 = fingers_spin[0]
spin2_2 = fingers_spin[1]
spin3_2 = fingers_spin[2]
spin4_2 = fingers_spin[3]
spin5_2 = fingers_spin[4]

roll1_2 = fingers_roll[0]
roll2_2 = fingers_roll[1]
roll3_2 = fingers_roll[2]
roll4_2 = fingers_roll[3]
roll5_2 = fingers_roll[4]

f.close()


print DTW(finger1_1, finger1_2)
print DTW(finger2_1, finger2_2)
print DTW(finger3_1, finger3_2)
print DTW(finger4_1, finger4_2)
print DTW(finger5_1, finger5_2)
print '/n'
print DTW(spin1_1, spin1_2)
print DTW(spin2_1, spin2_2)
print DTW(spin3_1, spin3_2)
print DTW(spin4_1, spin4_2)
print DTW(spin5_1, spin5_2)
print '/n'
print DTW(roll1_1, roll1_2)
print DTW(roll2_1, roll2_2)
print DTW(roll3_1, roll3_2)
print DTW(roll4_1, roll4_2)
print DTW(roll5_1, roll5_2)
print '/n'



