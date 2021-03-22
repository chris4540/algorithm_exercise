class Solution:
    records = {}

    def uniquePaths(self, m: int, n: int) -> int:
        for k in [(m, n), (n, m)]:
            if k in self.records:
                return self.records[k]

        if m == 1 or n == 1:
            return 1

        if m <= 0 or n <= 0:
            return 0
        # ------------------------

        ret = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        self.records[(m, n)] = ret
        self.records[(n, m)] = ret
        return ret

if __name__ == '__main__':
    fun = Solution().uniquePaths
    print(fun(3, 2))
    print(fun(7, 3))
    print(fun(3, 3))