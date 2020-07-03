"""
This method use:
    1. counting sort
    2. deque.


Counting sort is an algorithm for sorting a collection of objects according to keys that
are small integers.

Complexity: O(n+k), where n is the size of the array, k is the range of
the non-negative key values.

According to the problem, k <= 200 while ln(n) <= 17
Therefore, quick sort / merge sort is not useful at this case.

See:
https://en.wikipedia.org/wiki/Counting_sort

"""
from collections import deque


def get_median_from_cnts(count_arr, window_size):
    # print(count_arr)
    median_cnt = window_size // 2
    high = -1
    low = -1
    cnted = 0

    for e, cnt in enumerate(count_arr):

        if (window_size % 2 == 0) and cnted <= median_cnt-1 < cnted + cnt:
            low = e
        if cnted <= median_cnt < cnted + cnt:
            high = e

        # return if low and high are filled
        if window_size % 2 == 0 and low != -1 and high != -1:  # even number
            # print(low, high)
            return 0.5 * (low+high)
        elif window_size % 2 == 1 and high != -1:
            return high

        cnted += cnt

# def get_median_from_cnts(idx_counts, d):
#     d_half_floored = d // 2
#     median_low = 0
#     median_high = 0
#     traversed_elements = idx_counts[0]

#     idx = 1
#     while traversed_elements <= d_half_floored:
#         median_high = idx
#         if traversed_elements < d_half_floored:
#             median_low = idx  # still too low

#         traversed_elements += idx_counts[idx]
#         idx += 1

#     if d % 2 != 0:
#         return median_high  # d is odd
#     else:
#         return (median_low + median_high) / 2  # d is even


def activityNotifications(expenditure, d):
    """
    Args:
        exp (List[int]):
        d (int): window size
    """

    # # of notification
    ret = 0

    # build the counting array
    max_val = max(expenditure)
    cnts = [0] * (max_val+1)

    # rolling window
    roll_win = deque([], maxlen=d)
    # loop over the rolling window
    for spend in expenditure:

        if len(roll_win) >= d:
            # calcuate the median from the cnt arr
            median = get_median_from_cnts(cnts, d)
            # print("median = ", median)
            # print(roll_win)
            if spend >= 2*median:
                ret += 1
            # --------
            # remove
            # --------
            element = roll_win.popleft()
            cnts[element] -= 1

        # --------
        # Append
        # --------
        # update rolling window
        roll_win.append(spend)
        # update counting
        cnts[spend] += 1

    return ret


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
