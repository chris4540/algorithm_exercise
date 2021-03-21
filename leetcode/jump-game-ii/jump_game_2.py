"""
https://leetcode.com/problems/jump-game-ii/

Notes:
Do the problem from backward to the first

The end portion of the array can be consider a subproblem
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        # edge case, trap at the start
        if nums[0] == 0:
            return 0
        if len(nums) == 1:
            return 0

        length = len(nums)
        dp = [length] * length  # the number of ways at each position
        dp[-1] = 1  # base case

        for i in range(len(nums)-2, -1, -1):
            steps = nums[i]
            if steps + i >= length - 1:
                dp[i] = 1
            elif steps == 0:
                continue
            else:
                # search the range
                for j in range(1, steps+1):
                    jump = dp[i+j] + 1
                    if dp[i] > jump:
                        dp[i] = jump

        print(dp)
        return dp[0]

if __name__ == '__main__':
    fun = Solution().jump
    print(fun([2,3,1,1,4]))
    print(fun([2,3,0,1,4]))
    print(fun([1, 2, 3]))