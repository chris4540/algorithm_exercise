
"""
Time Complexity: O(d + n) where n is the size of collection

Used greedy approach
"""


# Complete the hackerCards function below.
def hackerCards(collection, d):
    ret = []
    col_ptr = 0
    i = 1
    budget = d
    while i <= d and col_ptr < len(collection) and budget > 0:
        if i == collection[col_ptr]:
            i += 1
            col_ptr += 1 if col_ptr < len(collection)-1 else 0
        elif i > collection[col_ptr]:
            if col_ptr < len(collection)-1:
                col_ptr += 1
            else:
                # buy it
                ret.append(i)
                budget -= i
                i += 1
        elif i < collection[col_ptr]:
            # buy it
            ret.append(i)
            budget -= i
            i += 1
    return ret

if __name__ == '__main__':

    collection_count = int(input().strip())
    collection = []
    for _ in range(collection_count):
        collection_item = int(input().strip())
        collection.append(collection_item)

    d = int(input().strip())
    res = hackerCards(collection, d)
    print(res)
