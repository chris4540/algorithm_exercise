from typing import List

class Solution:
    MAX_BOUND = 10**9 + 7

    def maxSubArray(self, arr: List[int]) -> int:
        ret = 0
        local_sum_max = 0
        for e in arr:
            local_sum_max = max(0, local_sum_max + e)
            ret = max(ret, local_sum_max)
        return ret

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        if k == 1:
            return self.maxSubArray(arr)

        # trival sol when all elements in the input array are +ve
        total = sum(arr)

        # we try to concat the arr twice and check the maximum subarr
        max_sub2arr = self.maxSubArray([*arr, *arr])

        # we have 3 cases:
        #       1. zero
        #       2. only the max subarr from the arr twice
        #       3. 2 + (k-2), which means we pick them all
        ret = max([0, max_sub2arr, max_sub2arr + total*(k-2)])
        ret = ret % self.MAX_BOUND
        return ret

if __name__ == '__main__':
    # res = Solution().kConcatenationMaxSum([1, 2], 3)
    # print(res)

    # res = Solution().kConcatenationMaxSum([1, -2, 1], 5)
    # print(res)

    # res = Solution().kConcatenationMaxSum([1, -1], 5)
    # print(res)

    res = Solution().kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4], 5)
    print(res)