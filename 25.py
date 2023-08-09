from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.val:
            return ""

        if not self.next:
            print(self.val)
        else:
            print(self.val, " -> ", self.next)

        return ""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head or not head.next:
            return head

        newhead = None
        cur1, cur2 = head, head.next
        pre = None

        def check_length(n: Optional[ListNode], min_len: int) -> bool:
            for _ in range(min_len - 1):
                if not n.next:
                    return False
                n = n.next

            return True

        while cur1:
            if not check_length(cur1, k):
                if not newhead:
                    newhead = head

                if pre:
                    pre.next = cur1

                break

            p1 = cur1
            for i in range(k - 1):
                tmp = cur1
                cur1, cur2 = cur2, cur2.next
                cur1.next = tmp

            if not newhead:
                newhead = cur1
                p1.next = None
            else:
                pre.next = cur1

            pre = p1
            if not cur2:
                break
            cur1, cur2 = cur2, cur2.next

        return newhead


if __name__ == '__main__':
    print(Solution().reverseKGroup(ListNode(1, ListNode(2)), 2))