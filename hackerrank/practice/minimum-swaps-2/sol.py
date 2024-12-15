#!/bin/python3
"""
Q: https://www.hackerrank.com/challenges/minimum-swaps-2
https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

https://www.youtube.com/watch?v=Mk9Fre9_f64&t=1269s

The critical insight is that each element can only be part of one swap operation
before it reaches its correct position. Therefore:

At first glance, it might seem like the nested while loop increases the time complexity to
𝑂(n**2). However, the key is that the total number of swaps
(iterations of the while loop) is bounded by n for the entire array, not per element.

Therefore, the whole algorithm is 𝑂(n)
"""


# Complete the minimumSwaps function below.
def minimumSwaps(arr: list[int]) -> int:
    ret = 0

    for i, n in enumerate(arr):

        # Swap iteratively until the correct answer inplace
        curr = n
        while curr != i + 1:
            # pick up the target one
            tmp = arr[curr-1]

            # put the current one into the right place
            arr[curr-1] = curr
            curr = tmp
            arr[i] = curr
            ret += 1

    return ret


if __name__ == '__main__':
    # arr = [4, 3, 1, 2]
    arr = [7, 1, 3, 2, 4, 5, 6]
    print(arr)
    x = minimumSwaps(arr)
    print(x)