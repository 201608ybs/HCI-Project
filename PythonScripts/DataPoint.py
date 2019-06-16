# coding:utf8


class DataPoint(object):
    def __init__(self, data):
        self.data = data


class TimeSequence(object):
    def __init__(self, data_points):
        self.data_points = data_points
