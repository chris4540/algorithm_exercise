"""
Topological sorting using DFS + recursion

https://leetcode.com/problems/course-schedule-ii/discuss/190393/Topological-Sort-Template-General-Approach!!
"""
from typing import List

class Solution:


    def _dfs(self, v, adj_list, visited, stack):

        # first mark the list to be true
        visited[v] = True

        for nei in adj_list[v]:
            if not visited[nei]:
                self._dfs(nei, adj_list, visited, stack)

        stack.append(v)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        # here we use the adjcenty list
        adj_list = {k: [] for k in range(numCourses)}


        # build the graph
        for u, v in prerequisites:
            adj_list[v].append(u)

        # ----------------------------------
        # Topological sorting with dfs
        # ----------------------------------
        visited = [False] * numCourses

        # The travaling history
        stack = []

        # loop over all vertices to make sure no vertex missed
        for i in range(numCourses):
            if not visited[i]:
                self._dfs(i, adj_list, visited, stack)

        ret = stack[::-1]
        return ret


if __name__ == '__main__':
    sol = Solution()
    # sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print(sol.findOrder(2, [[0, 1], [1, 0]]))