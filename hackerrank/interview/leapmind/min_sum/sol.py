#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heapify
from heapq import heappop
from heapq import heapreplace


#
# Complete the 'minSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY num
#  2. INTEGER k
#

def minSum(num, k):
    h = [-i for i in num]
    heapify(h)
    # greedy + heap
    print(h)
    for _ in range(k):

        max_val = h[0]   # which is in neg-val
        # replace the max one
        heapreplace(h, math.floor(max_val / 2))
        print(h)

    return -sum(h)

if __name__ == '__main__':
    num_count = int(input().strip())

    num = []

    for _ in range(num_count):
        num_item = int(input().strip())
        num.append(num_item)

    k = int(input().strip())

    result = minSum(num, k)

    print(result)
