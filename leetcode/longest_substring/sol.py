
def get_len_longest_substring(s: str) -> int:
    substr_char_set = set()
    ret = 0
    l = 0  # the left pointer

    # r is the right pointer
    for r, char in enumerate(s):
        while char in substr_char_set:
            substr_char_set.remove(s[l])
            l += 1
        substr_char_set.add(char)
        ret = max(ret, r - l + 1)
        print(s[l:r+1], r, l, ret)

    return ret


if __name__ == "__main__":
    # assert get_len_longest_substring("abcabcbb") == 3
    # assert get_len_longest_substring("bbbbb") == 1
    assert get_len_longest_substring("pwwkew") == 3
