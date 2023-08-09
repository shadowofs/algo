from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodemap = {}

        def deepcopy(n: Node) -> Node:
            if not n:
                return n

            nonlocal nodemap
            if n in nodemap:
                return nodemap[n]

            nn = Node(x=n.val)
            nodemap[n] = nn
            nn.next = deepcopy(n.next)
            nn.random = deepcopy(n.random)
            return nn

        return deepcopy(head)


if __name__ == '__main__':

    Solution().copyRandomList(Node(1, next=Node(2, next=Node(3))))