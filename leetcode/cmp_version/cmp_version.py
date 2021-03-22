"""
https://leetcode.com/problems/compare-version-numbers/
"""
from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1_arr: List[int] = [int(v) for v in version1.split(".")]
        ver2_arr: List[int] = [int(v) for v in version2.split(".")]

        num_version = max(len(ver1_arr), len(ver2_arr))

        for i in range(num_version):

            v1 = ver1_arr[i] if i < len(ver1_arr) else 0

            v2 = ver2_arr[i] if i < len(ver2_arr) else 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        # if no early return, they are the same
        return 0

if __name__ == '__main__':
    fun = Solution().compareVersion

    print(fun("1.01", "1.001"))
    print(fun("1.0", "1.0.0"))
    print(fun("0.1", "1.0"))
    print(fun("1.0.1", "1"))
    print(fun("7.5.2.4", "7.5.3"))