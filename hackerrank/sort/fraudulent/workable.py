from collections import deque

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    """k << d, n --> counting sort approach"""
    k = max(expenditure)
    historic_counts = [0] * (k+1)
    trailing_history = deque([])
    num_notifications = 0

    for day in range(len(expenditure)):
        if day >= d:
            if expenditure[day] >= 2 * median(historic_counts, d):
                num_notifications += 1

            historic_counts[trailing_history.popleft()] -= 1

        historic_counts[expenditure[day]] += 1
        trailing_history.append(expenditure[day])
        print(trailing_history)

    return num_notifications

def median(idx_counts, d):
    d_half_floored = d // 2
    median_low = 0
    median_high = 0
    traversed_elements = idx_counts[0]

    idx = 1
    while traversed_elements <= d_half_floored:
        median_high = idx
        if traversed_elements < d_half_floored:
            median_low = idx  # still too low

        traversed_elements += idx_counts[idx]
        idx += 1

    if d % 2 != 0:
        return median_high  # d is odd
    else:
        return (median_low + median_high) / 2  # d is even

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)
