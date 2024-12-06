"""
https://www.freecodecamp.org/news/how-to-solve-the-sherlock-and-anagrams-coding-challenge-in-javascript-a80baa908637/
"""
from collections import Counter, defaultdict
from _collections_abc import dict_values
import string

class LowerCaseCharacterCounter:

    counter: dict[str, int]
    def __init__(self, s: str) -> None:
        self.counter = dict.fromkeys(string.ascii_lowercase, 0)

        for c in s:
            self.counter[c.lower()] += 1

    def __getitem__(self, key: str) -> int:
        return self.counter[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.counter[key] = value


    def values(self) -> dict_values:
        return self.counter.values()

    def encoded(self) -> tuple[int, ...]:
        """Return the encoding using counts of the given string
        Thus, the same anagram share the same encoding.
        """
        return tuple(self.counter.values())


def sherlockAndAnagrams(s: str) -> int:
    anagram_count = 0

    for window_size in range(1, len(s)):
        counter = LowerCaseCharacterCounter(s[:window_size])

        encoding = counter.encoded()
        snapshots = defaultdict(lambda: 0)
        snapshots[encoding] += 1

        # Moving to the next window
        for i in range(1, len(s) - window_size + 1):
            j = i + window_size - 1
            counter[s[i-1]] -= 1
            counter[s[j]] += 1

            encoding = counter.encoded()
            # we accumulate counts since we count the permutations rather than the combinations.
            anagram_count += snapshots[encoding]
            snapshots[encoding] += 1

    return anagram_count



if __name__ == '__main__':
    x = sherlockAndAnagrams("abba")
    print(x)

    # print(is_anagram("abba", "abab"))