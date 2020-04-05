"""
Key:
    Consider at any time s, the time interval [s, s+1] has atmost 2 slots for
    Cameron and Jamie.
"""

def insert_timeslot_to_sch(schedule, timeslot):
    """
    Return True if inserted, vise-verse
    """
    if len(schedule) == 0:
        schedule.append(timeslot)
        return True

    # check if timeslot is okay to insert
    last_endtime = schedule[-1][1]
    start_time = timeslot[0]
    if last_endtime <= start_time:
        schedule.append(timeslot)
        return True

    # failed
    return False


if __name__ == "__main__":

    num_test = int(input())
    for case in range(1, num_test+1):
        # read the number of slots
        n_slot = int(input())
        slots = list()
        for _ in range(n_slot):
            # ts: time-slot
            ts = tuple([int(i) for i in input().split()])
            slots.append(ts)
        # --------------------------------------------
        # sort by the start time for greedy assignment
        sorted_slot_idx = [i for i, t in sorted(enumerate(slots), key=lambda x:x[1][0])]

        # allocate two list as schedule to check their assignment
        cameron_sch = list()
        jamie_sch = list()
        decision = [None] * n_slot  # the representation of the assignment decision
        for i in sorted_slot_idx:
            ts = slots[i]
            if insert_timeslot_to_sch(cameron_sch, ts):
                decision[i] = "C"
            elif insert_timeslot_to_sch(jamie_sch, ts):
                decision[i] = "J"
            else:
                decision = ["IMPOSSIBLE"]
                break

        decision = ''.join(decision)
        print("Case #{}: {}".format(case, decision))


