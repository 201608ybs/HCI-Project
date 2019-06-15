import serial
import os,time
import DTW
import AP

serialPort = "COM3"
Rate = 57600
ser = serial.Serial(serialPort, Rate, timeout=0.5)
data = []
simple = []
i = 0

while i < 20:
    str = ser.readline()
    str = str.decode('utf-8')
    temp = str.split(' ')
    if len(temp) == 3:
        for index in range(3):
            try:
                temp[index] = float(temp[index])
                if len(data) >= 20 and index == len(temp) - 1:
                    data.remove(data[0])
                    data.append(temp)
                if len(data) < 20 and index == len(temp) - 1:
                    data.append(temp)
            except ValueError:
                continue
        if len(data) == 20:
            simple.append(data)
            data = []
            i += 1
            print i
R = AP.init_matrix_r(20)
A = AP.init_matrix_a(20)
simi = AP.cal_seq_list(simple)
print simi
class_cen = AP.cal_cluster_centers(20, simi, R, A)
print class_cen
