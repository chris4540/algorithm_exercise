# Complete the countSwaps function below.
def countSwaps(a):
    # counters
    n_swap = 0

    arr_len = len(a)

    for i in range(arr_len):
        for j in range(arr_len-1):
            if (a[j] > a[j+1]):
                # ---------------
                # swap them
                tmp = a[j+1]  # store a_{j+1}
                a[j+1] = a[j]
                a[j] = tmp
                # ---------------
                n_swap += 1

    print(f"Array is sorted in {n_swap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
