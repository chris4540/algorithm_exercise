"""
Not a good idea to have two sum for
"""

def binary_search(arr, x):
    """
    Iterative Binary Search Function
    It returns index of x in given array arr if present,
    else returns -1
    """
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

# Complete the whatFlavors function below.


def whatFlavors(cost, money):
    arg_sort = sorted(range(len(cost)), key=lambda k: cost[k])
    sorted_cost = [cost[i] for i in arg_sort]

    for s1 in range(1, money//2+1):
        i = binary_search(sorted_cost, s1)
        if i == -1:  # cannot find the element in sorted cost
            continue
        s2 = money - s1

        if s2 != s1:
            j = binary_search(sorted_cost, s2)
            if j == -1:
                continue
        else:
            # just do guessing as we must have unique ans
            for j in [i-1, i+1]:
                if sorted_cost[j] == s2:
                    break
        # ----------------
        # we got two index print out the index and break the loop

        # map back to org array idx and print it out
        a = arg_sort[i]
        b = arg_sort[j]
        if a > b:
            a, b = b, a
        print(a+1, b+1)
        return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
