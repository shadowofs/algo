# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root, None]
        line = []
        result = []
        while q:
            head = q.pop(0)
            while head:
                line.append(head.val)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
                head = q.pop(0)

            result.append(line)
            if not q:
                break
            q.append(None)
            line = []

        return result

if __name__ == '__main__':
    print(Solution().levelOrder((TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20)))))