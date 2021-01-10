from math import acos
from math import sqrt

def distance(x1, y1, x2, y2):
    ret = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return ret

def area_of_circular_segment(R, d):
    ret = (R**2)*acos(d/R) - d*sqrt(R**2 - d**2)
    return ret

def solution(x1, y1, r1, x2, y2, r2):

    if r1 > r2:
        R = r1
        r = r2
    else:
        R = r2
        r = r1

    d = distance(x1, y1, x2, y2)
    if (d - R - r) >= 1e-6:
        return 0.0

    # tangency condition
    if d == 0 or d <= R-r:
        return r**2

    d1 = (d**2 - r**2 + R**2) / (2*d)
    d2 = (d**2 + r**2 - R**2) / (2*d)
    ret = area_of_circular_segment(R, d1) + area_of_circular_segment(r, d2)
    return ret



if __name__ == '__main__':
    ret = solution(2, 2, 3, 5, 5, 3)
    print(ret)

    ret = solution(0, -2, 1, 0, 2, 1)
    print(ret)

    ret = solution(0, -1, 1, 0, 1, 1)
    print(ret)

    ret = solution(-1, 0, 10, -1, 1, 2)
    print(ret)
    (-2, 3, 4, 3, 3, 1)
    (-2, -4, 6, -2, -5, 5)

