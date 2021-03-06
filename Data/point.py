#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0, z=0):
        '''
        Input:
            [x, y, z] -> ZXY world
        '''
        self.x = x
        self.y = y
        self.z = z
        return

    def getNorm(self):
        norm2 = self.x * self.x + self.y * self.y + self.z * self.z
        return sqrt(norm2)

    def scale(self, scale_mul):
        scale = Point(self.x * scale_mul,
                      self.y * scale_mul,
                      self.z * scale_mul)
        return scale

    def inverse(self):
        inverse = Point(-self.x, -self.y, -self.z)
        return inverse

    def normalize(self):
        norm = self.getNorm()
        if norm == 0:
            return False
        self.x /= norm
        self.y /= norm
        self.z /= norm
        return True

    def add(self, point):
        self.x += point.x
        self.y += point.y
        self.z += point.z
        return True

    def toList(self):
        point_list = [self.x, self.y, self.z]
        return point_list

    def toArray(self):
        point_list = self.toList()
        point_array = np.array(point_list, dtype=np.float32)
        return point_array

    def outputInfo(self, info_level=0):
        line_start = "\t" * info_level

        print(line_start + "[Point]")
        print(line_start + "\t [" + \
              str(self.x) + ", " +\
              str(self.y) + ", " + \
              str(self.z) + "]")
        return True

