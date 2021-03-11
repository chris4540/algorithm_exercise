"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""
# def howManySwaps(arr):
#     # bubble sort
#     arr_len = len(arr)
#     cnt = 0
#     # print(arr)
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(1, arr_len):
#             if arr[i-1] > arr[i]:
#                 print(i-1, i)
#                 # print(i, j, arr[i], arr[j])
#                 # swap them
#                 arr[i-1], arr[i] = arr[i], arr[i-1]
#                 # print(arr)
#                 cnt += 1
#                 swapped = True
#         arr_len -= 1
#     # print(arr)
#     return cnt

def howManySwaps(arr):
    cnt = 0
    base = arr[0]
    for i, e in enumerate(arr):
        print(e - base)
        if (e - base > i):
            cnt += 1
    return cnt * 2

if __name__ == '__main__':
    assert howManySwaps([5, 1, 4, 2]) == 4
