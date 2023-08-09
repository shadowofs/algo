from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or len(preorder) == 0:
            return

        i = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break

        return TreeNode(val=preorder[0], left=self.buildTree(preorder=preorder[1:i+1], inorder=inorder[:i]),
                        right=self.buildTree(preorder=preorder[i+1:], inorder=inorder[i+1:]))


if __name__ == '__main__':
    print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))