"""
Prob:
https://leetcode.com/problems/decode-ways/

Explanation:
consider "12097":
for digit "1"    => # of ways = 1
for digit "12"   => # of ways = 2; [1, 2] and [12]
for digit "12"   => # of ways = 2; [1, 2] and [12]
for digit "129"  => # of ways = 2; [1, 2, 9] and [12, 9]
for digit "1297" => # of ways = 2; [1, 2, 9, 7] and [12, 9, 7]

Subproblem:
Can we split the last digit / last 2 digits?
If yes, then the number of ways increase / keep the same
"""

class Solution:

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        num_digits = len(s)

        if num_digits == 1 and s != "0":
            return 1

        if s.startswith("0"):
            return 0

        # build the memo array for dynamic programming
        # dp[i] => the number of ways of decode s[:i]
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, num_digits+1):
            # consider this digit
            if 0 < int(s[i-1:i]):
                dp[i] = dp[i-1]  # because we append this digit to the prev spliting

            # consider (i-1, i) two digits
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        print(dp)
        return dp[num_digits]


if __name__ == '__main__':
    fun = Solution().numDecodings
    # print(fun("10"))
    # print(fun("12"))
    # print(fun("226"))
    # print(fun("1297"))
    print(fun("2107"))
    print(fun("21007"))
