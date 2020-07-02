def binary_search_right(arr, l, r, key):
    while (r - l > 1):
        m = l + (r - l)//2
        if (arr[m] >= key):
            r = m
        else:
            l = m
    return r


def LongestIncreasingSubsequenceLength(arr):

    size = len(arr)
    #
    # tail_table = [0 for i in range(size + 1)]
    tail_table = [0] * (size+1)
    tail_table[0] = arr[0]
    ret = 1
    for i in range(1, size):
        if (arr[i] < tail_table[0]):
            # new smallest value
            tail_table[0] = arr[i]
        elif (arr[i] > tail_table[ret-1]):
            tail_table[ret] = arr[i]
            ret += 1
        else:
            tail_table[binary_search_right(tail_table, -1, ret-1, arr[i])] = arr[i]
    return ret


# Driver program to
# test above function

A = [2, 5, 3, 7, 11, 8, 10, 13, 6]
n = len(A)

print("Length of Longest Increasing Subsequence is ",
       LongestIncreasingSubsequenceLength(A))
