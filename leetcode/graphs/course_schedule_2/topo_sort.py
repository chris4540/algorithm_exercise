"""
Topological sorting using DFS + recursion

https://leetcode.com/problems/course-schedule-ii/discuss/190393/Topological-Sort-Template-General-Approach!!
"""
from typing import List

class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # here we use an adjcenty list to represent a graph
        adj_list = {k: [] for k in range(numCourses)}

        # and a map to save down the in-degree of each vertex
        indegree = {k: 0 for k in range(numCourses)}

        # build the graph and track the indegree of each vertex
        # an edge: (u, v) means the course `u` depends on the course `v`
        #  i.e.     u ----> v
        for u, v in prerequisites:
            adj_list[u].append(v)
            indegree[v] += 1

        # the sorted list
        topo_sorted = []

        # capture all nodes of indegree 0
        while indegree:
            cand = None
            for node, d in indegree.items():
                if d == 0:
                    cand = node
                    break
            # the indegree dictionary is not empty and candidate is None
            #   => We have a loop in the graph
            if cand is None and indegree:
                return []

            assert cand is not None

            # mark the candidate as shallow and "remove" the candidate from the graph
            indegree.pop(cand)
            topo_sorted.append(cand)

            # loop over acessible neigborhoods
            for nei in adj_list[cand]:
                indegree[nei] -= 1

        return topo_sorted[::-1]



if __name__ == '__main__':
    sol = Solution()
    # print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(sol.findOrder(2, [[0, 1], [1, 0]]))