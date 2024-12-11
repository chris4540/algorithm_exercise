"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/
"""
from collections import Counter

def makeAnagram(a: str, b: str) -> int:
    a_cnter = Counter(a)
    b_cnter = Counter(b)

    a_cnter.subtract(b_cnter)

    # consider the absolute values of the difference
    return sum(abs(v) for v in a_cnter.values())


if __name__ == '__main__':
    print(makeAnagram("abc", "cde"))
    print(makeAnagram("a", "aa"))
    print(makeAnagram("abc", "bca"))
    print(makeAnagram("cde", "def"))
