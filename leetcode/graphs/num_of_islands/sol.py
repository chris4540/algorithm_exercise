"""
https://leetcode.com/problems/number-of-islands/
"""
from typing import List


class Solution:

    def _dfs(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or i >= self.grid_long:
            return
        if j < 0 or j >= self.grid_width:
            return

        # mark visited grid as "#"
        if grid[i][j] == "1":
            grid[i][j] = "#"
            self._dfs(grid, i-1, j)
            self._dfs(grid, i+1, j)
            self._dfs(grid, i, j-1)
            self._dfs(grid, i, j+1)


    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        self.grid_long = len(grid)
        self.grid_width = len(grid[0])

        for i in range(self.grid_long):
            for j in range(self.grid_width):
                box = grid[i][j]
                if box == "1":
                    self._dfs(grid, i, j)
                    cnt += 1

        return cnt

if __name__ == '__main__':
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    sol = Solution()
    print(sol.numIslands(grid))