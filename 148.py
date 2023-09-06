# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def quickSort(head: Optional[ListNode]):
            if not head:
                return None, None
            if not head.next:
                return head, head

            preHead = None
            preTail = None
            tail = head
            cur = head.next

            while cur:
                if cur.val == head.val:
                    tmp = cur.next
                    cur.next = head
                    head = cur
                    cur = tmp
                elif cur.val > head.val:
                    tail.next = cur
                    tail = tail.next
                    cur = cur.next
                else:
                    if not preHead:
                        preHead = preTail = cur
                    else:
                        preTail.next = cur
                        preTail = preTail.next

                    cur = cur.next

            tail.next = None
            pre, cur = head, head.next
            while cur and pre.val == cur.val:
                pre, cur = pre.next, cur.next

            if cur:
                pre.next, tail = quickSort(cur)

            if not preHead:
                return head, tail

            preTail.next = None
            preHead, preTail = quickSort(preHead)
            preTail.next = head
            return preHead, tail

        head, tail = quickSort(head)
        return head


if __name__ == "__main__":
    print(Solution().sortList(ListNode(val=4, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=3))))))
