"""
46. Permutations

https://leetcode.com/problems/permutations/

Notes
-------
Consider the permutation tree.
At each level, we pick a number from the tray and never place back.
We form a tree and the easiest way to travel it is DFS

"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self._dfs(nums, [], ret)
        return ret

    def _dfs(self, nums: List[int], path, out):

        # basic case for recursion
        if not nums:
            # we reach the bottom
            out.append(path)
            return

        for i in range(len(nums)):
            next_nums = nums[:i] + nums[i+1:]
            self._dfs(next_nums, path + [nums[i]], out)

if __name__ == '__main__':
    fun = Solution().permute
    print(fun([1, 2, 3]))
