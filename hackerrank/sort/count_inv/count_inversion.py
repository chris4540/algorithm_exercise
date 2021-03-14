"""
Basically, this problem is sorting problem but in different version.

Readers easily goes to bubble sort yet merge sort should be more fessible.

This solution works if using pypy3
"""

def is_sorted(arr) -> bool:
    prev_e = arr[0]
    for e in arr[1:]:
        if prev_e > e:
            return False

        prev_e = e
    return True

def countInversions(arr) -> int:
    if len(arr) < 2:
        return 0

    if is_sorted(arr):
        return 0

    return merge_sort(arr)

def merge_sort(arr):
    ret = 0     # inversion count

    arr_len = len(arr)
    if arr_len < 2:
        return 0

    # divide
    mid = arr_len // 2
    arr1 = arr[0:mid]
    arr2 = arr[mid:arr_len]

    # conquer
    ret += merge_sort(arr1)
    ret += merge_sort(arr2)
    ret += _merge(arr1, arr2, arr)
    return ret

def _merge(arr1, arr2, out) -> int:
    """
    Merge two sorted Python lists S1 and S2 into properly sized list S.
    """
    i = 0
    j = 0
    ret = 0  # inversion count
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    out_len = len(out)
    while i + j < out_len:
        if j == arr2_len or (i < arr1_len and arr1[i] <= arr2[j]):
            # consider arr1[i] < arr2[j]
            out[i+j] = arr1[i]
            i += 1
        else:
            ii = i if i < arr1_len else arr1_len-1

            if arr1[ii] > arr2[j]:
                ret += len(arr1) - ii

            out[i+j] = arr2[j]
            j += 1
    # print(ret, out)
    return ret



if __name__ == '__main__':
    # arr = [1, 20, 6, 4, 5]
    # arr = [2, 1, 3, 1, 2]
    # arr = [1, 5, 3, 7]
    arr = [7, 5, 3, 1]
    # countInversions(arr)
    print(countInversions(arr))
    print(arr)