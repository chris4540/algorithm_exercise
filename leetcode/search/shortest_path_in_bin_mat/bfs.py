"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

The simplest BFS algorithm
"""
from typing import List, Tuple


class Solution:

    @staticmethod
    def _get_neigborhood_indices(i: int, j: int) -> List[Tuple[int, int]]:
        ret = []
        # total eight directions
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ret.append((i+di, j+dj))
        return ret

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n-1][n-1]:
            return -1

        queue = [(0, 0, 1)]
        # mark grid visited
        grid[0][0] = 1

        while queue:
            x, y, d = queue.pop(0)
            if x == n - 1 and y == n - 1:
                return d
            for i, j in self._get_neigborhood_indices(x, y):
                if 0 <= i < n and 0 <= j < n:
                    if grid[i][j] == 0:
                        grid[i][j] = 1  # mark as visited
                        queue.append((i, j, d+1))
        return -1

if __name__ == '__main__':
    fun = Solution().shortestPathBinaryMatrix

    # grid = [[0,1],[1,0]]
    # assert fun(grid) == 2


    # grid = [[0,0,0],[1,1,0],[1,1,0]]
    # assert fun(grid) == 4

    grid = [[1,0,0],[1,1,0],[1,1,0]]
    assert fun(grid) == -1
    grid = [[0]]
    assert fun(grid) == 1