def solution(A, K):
    n = len(A)
    best = 0
    count = 1
    for i in range(n - K - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
            count = 1
        best = max(best, count)
    print("best: ", best)
    result = best + K

    return result

if __name__ == '__main__':
    # arr = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
    # k = 2
    # ret = solution(arr, k)
    # print(ret)

    # arr = [1, 1, 1, 1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
    # k = 2
    # ret = solution(arr, k)
    # print(ret)

    # arr = [1, 1, 1, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 7]
    # k = 2
    # ret = solution(arr, k)
    # print(ret)

    # arr = [1, 1, 1, 3, 3, 4]
    # k = 6
    # ret = solution(arr, k)
    # print(ret)

    # arr, k = ([1, 2, 3, 4, 5, 6, 7, 8], 2)
    # arr, k = ([1, 1, 1, 1, 5, 6, 7, 8], 4)
    # arr, k = ([1, 1, 8, 8, 8, 8], 4)
    # arr, k = ([1, 1, 8, 8, 8, 8], 1)
    arr, k = ([1, 1, 8, 8, 8, 8], 1)
    ret = solution(arr, k)
    print(ret)