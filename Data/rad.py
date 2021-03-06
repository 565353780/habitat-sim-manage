#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class Rad(object):
    def __init__(self,
                 up_rotate_rad=0.0,
                 right_rotate_rad=0.0,
                 front_rotate_rad=0.0
                 ):
        self.up_rotate_rad = up_rotate_rad
        self.right_rotate_rad = right_rotate_rad
        self.front_rotate_rad = front_rotate_rad
        return

    def add(self, rad):
        self.up_rotate_rad += rad.up_rotate_rad
        self.right_rotate_rad += rad.right_rotate_rad
        self.front_rotate_rad += rad.front_rotate_rad
        return True

    def toList(self):
        rad_list = [self.up_rotate_rad, self.right_rotate_rad, self.front_rotate_rad]
        return rad_list

    def toArray(self):
        point_list = self.toList()
        point_array = np.array(point_list, dtype=np.float32)
        return point_array

    def outputInfo(self, info_level=0):
        line_start = "\t" * info_level

        print(line_start + "[Rad]")
        print(line_start + "\t up_rotate_angle = " + \
              str(np.rad2deg(self.up_rotate_rad)))
        print(line_start + "\t right_rotate_angle = " + \
              str(np.rad2deg(self.right_rotate_rad)))
        print(line_start + "\t front_rotate_angle = " + \
              str(np.rad2deg(self.front_rotate_rad)))
        return True

