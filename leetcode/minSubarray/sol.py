""" Just prefix sum within the modual group (%p)
"""
from typing import List

def minSubarray(nums: List[int], p: int) -> int:
    arr_sum = sum(nums)
    print(arr_sum)
    if arr_sum % p == 0:
        return 0

    if arr_sum < p:
        return -1
    # --------------
    # Dynamic Programming version
    # --------------
    need = arr_sum % p
    dp = {0: -1}  # the start pointer index before the list
    num_len = len(nums)
    ret = num_len
    cur = 0
    print(need)
    for i, a in enumerate(nums):
        cur = (cur + a) % p   # ring group of the reminder
        dp[cur] = i
        print(cur, i)
        if (cur - need) % p in dp:
            print("**", (cur-need) % p, i)
            ret = min(ret, i - dp[(cur - need) % p])
    if ret < num_len:
        return ret
    return -1

if __name__ == "__main__":
    # assert minSubarray([3,1,4,2], 6) == 1
    # assert minSubarray([6,3,5,2], 9) == 2
    # assert minSubarray([1, 2, 3], 3) == 0
    # assert minSubarray([1, 2, 3], 7) == -1
    # assert minSubarray([1000000000,1000000000,1000000000], 3) == 0
    assert minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2], 148) == 7
