# -*- coding: utf-8 -*-
import serial
import datetime


def init_port():
    serial_port = "COM4"
    baud_rate = 9600
    my_serial = serial.Serial(serial_port, baud_rate, timeout=0.5)
    return my_serial


def receive_data(receive_serial):
    f = open("hou-data4-8\-e.txt", 'w')
    flag1 = 0
    flag2 = 0

    while True:
        time_str = datetime.datetime.now().strftime('%H:%M:%S')
        line = receive_serial.readline()
        line = line.decode()
        datapoint_list = line.split(',')
        datapoint_list_without4 = datapoint_list[0:9] + datapoint_list[12:]
        line_without4 = ",".join(datapoint_list_without4)
        if line.count(',') == 19 and "0.00,0.00,0.00" not in line_without4:
            flag1 = 1
        if flag1 != flag2:
            print("数据采集正常!")
            flag2 = flag1
        if flag1:
            line = time_str + "," + line
            f.write(line)
            f.flush()


if __name__ == "__main__":
    receive_serial = init_port()
    receive_data(receive_serial)
