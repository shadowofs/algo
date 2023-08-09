class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = [root, None]
        while queue:
            top = queue[0]
            queue = queue[1:]
            while top:
                top.next = queue[0]
                if top.left:
                    queue.append(top.left)

                if top.right:
                    queue.append(top.right)

                top = queue[0]
                queue = queue[1:]
            if queue:
                queue.append(None)

        return root

if __name__ == "__main__":
    print(Solution().connect(Node(val=1, left=Node(val=2, left=Node(val=4), right=Node(val=5)), right=Node(val=3, right=Node(val=7)))))
