from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        pre, head = head, head.next
        pre.next = None
        while head:
            head, head.next, pre = head.next, pre, head

        return pre


if __name__ == "__main__":
    print(Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
