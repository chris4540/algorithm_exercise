class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}

        n = len(s)
        assert len(t) == n

        for i in range(n):
            s_i = s[i]
            t_i = t[i]
            if s_i not in s2t and t_i not in t2s:
                s2t[s_i] = t_i
                t2s[t_i] = s_i
            else:
                # checking
                if s_i in s2t and s2t[s_i] != t_i:
                    return False
                if t_i in t2s and t2s[t_i] != s_i:
                    return False

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isIsomorphic("egg", "add")
    assert sol.isIsomorphic("paper", "title")
    assert not sol.isIsomorphic("foo", "bar")
    assert not sol.isIsomorphic("badc", "baba")
