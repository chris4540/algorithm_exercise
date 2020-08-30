class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        n = self
        while n:
            print(n.val, end="")
            n = n.next
            if n:
                print("->", end="")
        print("")


def swap_nodes(node: ListNode) -> ListNode:
    # swap this node and the next node

    # terminal case 1: we go to the end
    if node is None:
        return None

    # terminal case 2: we don't have next, cancel swap
    if node.next is None:
        return node

    # -------------------------
    # swap node and the next ndoe
    first = node.next
    second = node
    second.next = swap_nodes(first.next)  # swap the children first
    first.next = second  # implement swap
    return first


def test_arr(arr):
    # build link list
    head = ListNode(arr[0])
    prev = head
    for x in arr[1:]:
        node = ListNode(x)
        prev.next = node
        prev = node

    # head.print()
    swap_nodes(head).print()

if __name__ == "__main__":
    test_arr([1, 2, 3, 4])
    test_arr([1, 2, 3, 4, 5])


