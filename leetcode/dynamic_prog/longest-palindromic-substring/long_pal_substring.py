"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    """ This solution is O(n**2) time complexity and O(n**2) space complexity
    """

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 1:
            return s
        # ----------------------
        # create the table to check if the string is palindrome
        dp_table = [[False for i in range(length)] for j in range(length)]

        # the basic case that the diagonal terms are palindrome
        for i in range(length):
            dp_table[i][i] = True

        # =======================================
        # consider len(ret) = 2
        ret = s[0]
        for i in range(length-1):
            if s[i] == s[i+1]:
                dp_table[i][i+1] = True
                ret = s[i:i+2]
        if length == 2 and len(ret) > 1:
            return ret
        # =======================================


        # consider len(ret) >= 3
        for k in range(3, length+1):  # the length of the candidate string
            for i in range(0, length - k + 1): # loop from start to n-k position
                # j is the perspective end char index of the candidate string
                j = i + k - 1

                # ----------------------
                # fill out the dp table
                # ----------------------
                # Example:
                # i = 4; j=8; sub = "xabcx" is a Palindrome string iff
                # 1. i=5; j=7 is a Palindrome string *and* s[4] == s[8]
                if (s[i] == s[j] and dp_table[i+1][j-1]):
                    dp_table[i][j] = True
                    if len(ret) < k:
                        ret = s[i:j+1]

        return ret




if __name__ == "__main__":
    fun = Solution().longestPalindrome
    # print(fun("babad"))
    # print(fun("cbbd"))
    # print(fun("a"))
    # print(fun("forgeeksskeegfor"))
    print(fun("ccc"))
