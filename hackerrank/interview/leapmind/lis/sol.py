#!/bin/python
"""
Longest Increasing Subsequence Size (N log N)

https://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""

# Complete the function below.


def findLIS(arr):
    ret = 0  # the counter the count logest increasing elements
    for i in range(len(arr)):
        if arr[i-1] < arr[i]:
            ret += 1
    return ret



if __name__ == "__main__":
    _s_cnt = int(input())
    _s_i = 0
    _s = []
    while _s_i < _s_cnt:

        _s_item = int(input())
        _s.append(_s_item)
        _s_i += 1


    res = findLIS(_s)
    print(res)
