import numpy as np

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # just in case we have to remove all characters to form word1 to word2
        word1 = "-" + word1
        word2 = "-" + word2

        m = len(word1)
        n = len(word2)
        # build up the
        dist = np.zeros((m, n), dtype=int)

        # edge case
        dist[:, 0] = np.arange(m)
        dist[0, :] = np.arange(n)


        for i in range(1, m):
            for j in range(1, n):
                r = 0
                if word1[i] != word2[j]:
                    r = 1
                # calculate the cost of operation
                cost = min(dist[i-1, j-1] + r, dist[i-1, j] + 1, dist[i, j-1] + 1)
                dist[i, j] = cost

        return dist[m-1, n-1]

if __name__ == '__main__':
    fun = Solution().minDistance

    print(fun("horse", "ros"))
    print(fun("zoologicoarchaeologist", "zoogeologist"))
