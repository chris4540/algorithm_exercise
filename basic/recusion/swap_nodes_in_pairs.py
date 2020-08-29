class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        n = self
        while n:
            print(n.val, end="")
            print("->", end="")
            n = n.next
        print("")

def swap_nodes(node: ListNode) -> ListNode:
    # swap this node and the next node
    if node is None or node.next is None:
        return None

    # -------------------------
    # swap node and the next ndoe
    first = node.next
    second = node
    second.next = swap_nodes(first.next)  #  swap the children first 
    first.next = second  # implement swap
    return first
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4]

    # build link list
    head = ListNode(arr[0])
    prev = head
    for x in arr[1:]:
        node = ListNode(x)
        prev.next = node
        prev = node
    
    head.print()
    head2 = swap_nodes(head)
    head2.print()