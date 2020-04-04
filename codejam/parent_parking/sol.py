from heapq import heappush
from bisect import bisect_left
from bisect import bisect_right


def is_period_overlap(p1, p2):
    """
    Check if two period are overlap

    Args:
        p1 (tuple[int]): like this (start, end)
        p2 (tuple[int]): like this (start, end)
    """
    s1, e1 = p1
    s2, e2 = p2

    if s1 > s2:
        # swap them
        s1, s2 = s2, s1
        e1, e2 = e2, e1

    overlap = False

    # there is one case they are not overlapping, e1 <= s2
    if e1 > s2:
        overlap = True

    return overlap


def test_is_period_overlap():
    assert is_period_overlap((360, 480), (420, 540)) == True
    assert is_period_overlap((420, 540), (360, 480)) == True

    #
    assert is_period_overlap((360, 480), (600, 660)) == False
    assert is_period_overlap((600, 660), (420, 540)) == False

    #
    assert is_period_overlap((0, 1440), (1, 3)) == True
    assert is_period_overlap((1, 3), (0, 1440)) == True
    #
    assert is_period_overlap((0, 4), (0, 1440)) == True
    assert is_period_overlap((0, 1440), (0, 4)) == True

    #
    assert is_period_overlap((0, 4), (2, 4)) == True
    assert is_period_overlap((2, 4), (1, 4)) == True

    #
    assert is_period_overlap((500, 501), (500, 501)) == True
    assert is_period_overlap((200, 500), (200, 500)) == True

    #
    assert is_period_overlap((200, 500), (200, 300)) == True
    assert is_period_overlap((200, 300), (200, 500)) == True

    #
    assert is_period_overlap((200, 300), (300, 500)) == False
    assert is_period_overlap((300, 500), (200, 300)) == False

    #
    assert is_period_overlap((500, 600), (600, 700)) == False

    assert is_period_overlap((500, 1000), (600, 700)) == True
    #
    assert is_period_overlap((400, 600), (250, 1000)) == True


def insert_to_pq(pq, period):
    inserted = False

    if len(pq) == 0:
        pq.append(period)
        inserted = True
        return inserted

    # bisection search
    insert_pt = bisect_left(pq, period)
    # print(insert_pt)
    # print(pq, period)
    if insert_pt == 0:
        # check the first one
        is_overlaped = is_period_overlap(period, pq[0])
    elif insert_pt == len(pq):
        # check the last one
        is_overlaped = is_period_overlap(period, pq[len(pq) - 1])
    else:
        # check before and after
        is_overlaped = is_period_overlap(period, pq[insert_pt])
        is_overlaped = is_overlaped or is_period_overlap(
            period, pq[insert_pt - 1])

    if not is_overlaped:
        # insertion
        pq.insert(insert_pt, period)
        inserted = True

    return inserted


if __name__ == "__main__":
    # test_is_period_overlap()
    num_test = int(input())
    for case in range(1, num_test + 1):
        # read the number of slots
        n_slot = int(input())
        slots = list()
        for _ in range(n_slot):
            period = [int(i) for i in input().split()]
            period = tuple(period)
            slots.append(period)
        # ---------------------------
        sorted_idx = [i  for i, t in sorted(enumerate(slots), key=lambda t:t[1][0])]
        # make two priority queue
        cameron_pq = list()
        jamie_pq = list()

        decision = "" 
        sch_slots = dict()
        
        for i in sorted_idx:
            period = slots[i]
            # try insert to cameron_pq
            inserted = insert_to_pq(cameron_pq, period)
            if inserted:
                sch_slots[i] = "C"
                # decision += "C"
            else:
                # try insert to jamie_pq
                inserted = insert_to_pq(jamie_pq, period)
                if inserted:
                    sch_slots[i] = "J"
                    # decision += "J"
                else:
                    decision = "IMPOSSIBLE"
                    break
        
        if decision != "IMPOSSIBLE":
            for i in range(len(slots)):
                decision += sch_slots[i]
        print("Case #{}: {}".format(case, decision))
