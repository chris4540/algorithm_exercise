from tool import linked_list_factory
from tool import ListNode
from tool import to_list




class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        placeholder = 0

        cur_1 = l1
        cur_2 = l2

        # max_iters = max(len(l1), len(l2)) + 10

        head = ListNode()
        cur = head

        while True:
            sum_ = placeholder

            if cur_1:
                sum_ += cur_1.val

            if cur_2:
                sum_ += cur_2.val
            # -----------------------------
            result_digit = sum_ % 10
            placeholder = sum_ // 10

            cur.val = result_digit

            # move to next node
            if cur_1 is not None:
                cur_1 = cur_1.next
            if cur_2 is not None:
                cur_2 = cur_2.next

            if cur_1 or cur_2 or placeholder != 0:
                next_node = ListNode()
                cur.next = next_node
                cur = next_node
            else:
                break

        return head
if __name__ == '__main__':
    l1 = linked_list_factory([9,9,9,9,9,9,9])
    l2 = linked_list_factory([9,9,9,9])

    fun = Solution().addTwoNumbers

    ll = fun(l1, l2)
    print(to_list(ll))