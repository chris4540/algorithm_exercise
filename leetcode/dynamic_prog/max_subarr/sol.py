from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ Consider the solution using dynamic programming
        """

        local_sum_max = 0     # this is the local subarray maximum
        sum_max = nums[0]     # this is the global maximum we track.
                              # We can use -inf or the first element of the input
                              # arr.


        for e in nums:
            # reset the sum if the sum of the contingous array goes to -ve number
            local_sum_max = max(e, local_sum_max + e)
            sum_max = max(sum_max, local_sum_max)
        return sum_max

if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    res = Solution().maxSubArray(arr)
    assert res == 6

    arr = [-1, -2]
    res = Solution().maxSubArray(arr)
    assert res == -1