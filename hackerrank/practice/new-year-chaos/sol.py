#!/bin/python3
"""
https://www.hackerrank.com/challenges/new-year-chaos/
"""

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    for final_pos, start_pos in enumerate(q):
        # Abort if anyone is more than two bribes ahead of where they started
        if  final_pos + 1 < start_pos - 2:
            print('Too chaotic')
            return
        # Count the number of people who started behind me, who are ahead of my
        # final position. Conduct the search between two spots forward of where
        # I started, thru to the person in front of me in the end; as these are
        # the only people to have potentially bribed me.
        potential_bribers = range(max(start_pos - 2, 0), final_pos)
        bribes += [q[briber] > start_pos for briber in potential_bribers].count(True)
    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
