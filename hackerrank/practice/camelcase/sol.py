"""
https://www.hackerrank.com/challenges/camelcase/problem
"""
def camelcase(s: str) -> int:
    if len(s) == 0:
        return 0

    # There are a least one word
    ret = 1

    for c in s:
        if c.isupper():
            ret += 1
    return ret


if __name__ == '__main__':
    print(camelcase("saveChangesInTheEditor"))