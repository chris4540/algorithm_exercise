from math import atan2
class Point2d:
    x = 0
    y = 0

def get_polar_angle(point_2d):
    return atan2(point_2d.y, point_2d.x)