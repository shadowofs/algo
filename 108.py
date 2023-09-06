# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(val=nums[0])

        mid = int(len(nums) / 2)
        left = self.sortedArrayToBST(nums=nums[:mid])
        right = self.sortedArrayToBST(nums=nums[mid + 1:])

        return TreeNode(val=nums[mid], left=left, right=right)


if __name__ == "__main__":
    print(Solution().sortedArrayToBST([1,2,3]))