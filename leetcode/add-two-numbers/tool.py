from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(head: ListNode):
    results = []
    cur = head
    while cur:
        results.append(cur.val)
        cur = cur.next

    return results

def linked_list_factory(nums: List[int]) -> ListNode:
    head = ListNode()
    if not nums:
        return head

    head.val = nums[0]
    cur = head
    for n in nums[1:]:
        new_node = ListNode(n)
        cur.next = new_node
        cur = new_node

    return head



if __name__ == '__main__':
    head = linked_list_factory([1, 2, 3])

    print(to_list(head))