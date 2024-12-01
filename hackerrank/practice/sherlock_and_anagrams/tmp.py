"""
https://www.freecodecamp.org/news/how-to-solve-the-sherlock-and-anagrams-coding-challenge-in-javascript-a80baa908637/
"""
from collections import Counter

def sherlockAndAnagrams(s) -> int:
    char_counter = Counter(s)
    anagrams = set()
    ret = 0
    # Write your code here
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]

            if substring in anagrams:
                print(substring)
                ret += 1
                continue

            substring_counter = Counter(substring)

            # check if the substring is an anagram by char counter inclusion checking
            if substring_counter <= char_counter:
                anagrams.add(substring)



    return ret

if __name__ == '__main__':
    x = sherlockAndAnagrams("ifailuhkqq")
    print(x)