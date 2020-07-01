"""
This method use counting sort as well as queue.

It is an algorithm for sorting a collection of objects according to keys that
are small integers.

Complexity: O(n+k), where n is the size of the array, k is the range of
the non-negative key values.

According to the problem, k <= 200 while ln(n) <= 17
Therefore, quick sort / merge sort is not useful at this case.


See:
https://en.wikipedia.org/wiki/Counting_sort

Sorting-Fraudulent Activity Notifications
!!!!!!!!!!!!!!!!!
Not completed yet
!!!!!!!!!!!!!!!!!
"""


# def counting_sort(array):
#     max_val = max(array)

#     # build the count array
#     cnts = [0] * (max_val+1)
#     for x in array:
#         cnts[x] += 1

#     # build the cummulative count
#     for i in range(1, max_val+1):
#         cnts[i] += cnts[i-1]
#     # alias
#     cm_cnts = cnts

#     # build return
#     ret = [None] * len(array)
#     for x in array:
#         # get the sorted index
#         idx = cm_cnts[x] - 1
#         ret[idx] = x

#         # reduce the count as we have used; for duplicated elements
#         cm_cnts[x] -= 1
#     return ret

def get_median_from_idx_cnt(idx_cnt_arr, window_size):
    mid = window_size // 2
    # two pointers to find high and low for the median
    if window_size % 2 == 1:
        # odd
        i_ptr = mid  # just duplicate two placement
        j_ptr = mid
    else:
        i_ptr = mid
        j_ptr = mid+1

    ret = 0


    for x, cnt in enumerate(idx_cnt_arr):
        if i_ptr >= cnt:
            i_ptr -= cnt
        elif i_ptr != -1:
            ret += x
            i_ptr = -1

        if j_ptr >= cnt:
            j_ptr -= cnt
        elif j_ptr != -1:
            ret += x
            j_ptr = -1

        if i_ptr == -1 and j_ptr == -1:
            break

    return ret / 2


def cnts_to_arr(cnts, d):
    ret = []
    for x, cnt in enumerate(cnts):
        if cnt > 0:
            ret.extend([x] * cnt)
    return ret


def activityNotifications(expenditure, d):
    """
    Args:
        exp (List[int]):
        d (int): window size
    """

    # counting
    n_notification = 0

    # build the first counting array
    max_val = max(expenditure)
    arr = expenditure[:d]
    cnts = [0] * (max_val+1)
    for x in arr:
        cnts[x] += 1
    # --------------------------

    # loop over the rolling window
    for i in range(d, len(expenditure)):
        spend = expenditure[i]
        # print(expenditure[i-d:i])
        # arr = cnts_to_arr(cnts, d)
        # print(arr)
        median = get_median_from_idx_cnt(cnts, d)
        # print(median)
        if spend >= 2*median:
            n_notification += 1

        # tidy up the count arr
        # subtract cnt of the prev. element
        # print("-------------")
        # print(expenditure[i-d])
        cnts[expenditure[i-d]] -= 1
        # add cnt to the current element
        # print(expenditure[i])
        cnts[expenditure[i]] += 1
        # print("-------------")

    return n_notification


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
