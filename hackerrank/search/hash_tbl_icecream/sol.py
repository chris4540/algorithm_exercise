def whatFlavors(cost, money):
    """
    This is just a two-sum problem
    """
    sums = []
    hash_table = dict()
    for i, s1 in enumerate(cost):
        if sums:
            break  # early exit

        s2 = money - s1

        if s2 in hash_table:
            # we found the pair!
            sums.append((i, hash_table[s2]))

        # save down the cost element and the index
        hash_table[s1] = i
    # --------------------------------
    a, b = sums[0]
    if a > b:
        a, b = b, a
    print(a+1, b+1)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
