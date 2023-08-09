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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_node = head
        left_pre = None

        if left >= 2:
            left_pre = head
            for i in range(left - 2):
                left_pre = left_pre.next

            left_node = left_pre.next
        pre, post = left_node, left_node.next
        for i in range(right - left):
            tmp = pre
            pre, post = post, post.next
            pre.next = tmp

        if left >= 2:
            left_pre.next, left_node.next = pre, post
        else:
            head, left_node.next = pre, post

        return head


if __name__ == "__main__":
    print(Solution().reverseBetween(ListNode(3, ListNode(5)), 1, 2))

