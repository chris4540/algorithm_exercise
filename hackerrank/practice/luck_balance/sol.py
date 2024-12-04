"""
https://www.hackerrank.com/challenges/luck-balance
"""
def luckBalance(k, contests):

    # Sort the contest first,
    # then we can just losing the important and high luckiness contest at the beginning
    contests.sort(key=lambda k: k[0], reverse=True)
    ret = 0

    num_won_important_match = 0

    for contest in contests:
        l = contest[0]
        t = contest[1]

        # Case 0: Unimportant test, just lose it
        if t == 0:
            ret += l
            continue

        # Case 1: important test, but we can lost it (since we sorted the contests)
        if t == 1 and num_won_important_match < k:
            ret += l
            num_won_important_match += 1
            continue

        # case 2: We need to spend luck to win the contest
        ret -= l

    return ret

if __name__ == '__main__':
    k = 3
    contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
    print(luckBalance(k, contests))  # Output: 13