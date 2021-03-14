class Solution:

    cap_a_ascii = ord("A")
    def charToNumber(self, charColumn: str) -> int:
        if len(charColumn) > 1:
            raise ValueError("Only accept one character as an input.")

        ret = ord(charColumn) - self.cap_a_ascii + 1
        return ret

    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        for c in columnTitle:
            ret = ret * 26 + self.charToNumber(c)
        return ret

if __name__ == '__main__':
    assert Solution().titleToNumber("A") == 1
    assert Solution().titleToNumber("AB") == 28
    assert Solution().titleToNumber("ZY") == 701
    assert Solution().titleToNumber("FXSHRXW") == 2147483647