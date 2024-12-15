#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter

def most_common_small_element(arr: list[int]) -> int:
    if not isinstance(arr, list):
        arr = list(arr)

    arr.sort()
    return max(arr, key=arr.count)

def isValid(s: str) -> str:
    char_counter = Counter(s)

    count_to_freq = Counter(char_counter.values())

    if len(count_to_freq) > 2:
        return "NO"

    if len(count_to_freq) == 1:
        return "YES"

    assert len(count_to_freq) == 2

    count1, count2 = count_to_freq.keys()
    if count1 > count2:
        # swap to make count1 is the smaller one
        count1, count2 = count2, count1

    freq1 = count_to_freq[count1]
    freq2 = count_to_freq[count2]
    if freq2 == 1 and count2 - count1 == 1:
        return "YES"

    # Edge case: only single alphabet is in string while all other have same frequency
    if freq1 == 1 and count1 == 1:
        return "YES"

    return "NO"

if __name__ == "__main__":
    test_str = "abcdefghhgfedecba"
    ans = isValid(test_str)
    print(ans)