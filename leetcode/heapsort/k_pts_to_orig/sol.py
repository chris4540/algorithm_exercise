"""
https://leetcode.com/problems/k-closest-points-to-origin/

Notes:
Use heap will be much easiler
"""
from heapq import heappushpop
from heapq import heappush

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for pt in points:
            x = pt[0]
            y = pt[1]
            dist_sq = x*x + y*y
            itm = (-dist_sq, (x, y))
            if len(heap) == k:
                heappushpop(heap, itm)
            else:
                heappush(heap, itm)

        ret = []
        for itm in heap:
            ret.append(itm[1])

        return ret
