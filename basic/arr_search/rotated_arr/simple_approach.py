"""
https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

  1) Find out pivot point and divide the array in two
      sub-arrays. (pivot = 2) /*Index of 5*/
  2) Now call binary search for one of the two sub-arrays.
      (a) If element is greater than 0th element then
             search in left array
      (b) Else Search in right array
          (1 will go in else as 1 < 0th element(3))
  3) If element is found in selected sub-array then return index
     Else return -1.
"""
from typing import List


def find_pivot_idx(arr: List[int]) -> int:
    """ Find the pivot point using binary search

    Example:
    >>> find_pivot_idx([3, 4, 5, 6, 1, 2])
    3  # becasue arr[3] is 6
    >>> find_pivot_idx([3, 4, 5, 6, 7, 8, 1, 2])
    55

    """

    def _find_pivot_idx_rec(arr: List[int], low: int, high: int):
        # base cases for recussion
        if high < low:
            return -1 # cannot find
        if high == low:
            return high
        # ----------------------------

        mid = (low + high) // 2
        print("mid=", mid)

        assert mid < high
        # consider if we pin-point the pivot
        if (arr[mid] > arr[mid+1]):
            return mid

        if (arr[mid-1]> arr[mid]):
            return mid-1


        if arr[low] >= arr[mid]:
            return _find_pivot_idx_rec(arr, low, mid-1)

        # if arr[mid+1] >= arr[high]:
        return _find_pivot_idx_rec(arr, mid+1, high)

    # -------------------
    ret = _find_pivot_idx_rec(arr, 0, len(arr)-1)
    if ret == -1:
        raise ValueError("Cannot find the pivot point.")

    return ret

if __name__ == '__main__':
    arr = [3, 4, 5, 6, 7, 8, 1, 2]
    res = find_pivot_idx(arr)
    print(res)