"""
https://www.hackerrank.com/challenges/count-triplets-1
"""
from collections import Counter

def countTriplets(arr, r):
    ret = 0

    g2 = Counter()  # The number of (a) to aR as key
    g3 = Counter()  # The number of (a, aR) to aR**2 as key

    for val in arr:
        if val in g3:
            ret += g3[val]

        if val in g2:
            g3[val*r] += g2[val]

        g2[val*r] += 1


    return ret


if __name__ == "__main__":
    arr = [1, 3, 9, 9, 27, 81]
    r = 3
    print(countTriplets(arr, 3))