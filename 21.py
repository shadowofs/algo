from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None

        def appendNext(n: Optional[ListNode]):
            nonlocal head
            nonlocal tail
            if not tail:
                tail = n
                head = n
            else:
                tail.next = n
                tail = n

        while list1 and list2:
            if list1.val <= list2.val:
                appendNext(list1)
                list1 = list1.next
            else:
                appendNext(list2)
                list2 = list2.next

        while list1:
            appendNext(list1)
            list1 = list1.next

        while list2:
            appendNext(list2)
            list2 = list2.next

        return head


if __name__ == '__main__':
    print(Solution)
