import math


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getMinMax(node: TreeNode) -> (int, int):
            leftMax = math.minint
            minV = node.val
            maxV = node.val
            if node.left:
                minV, leftMax = getMinMax(node.left)

                if minDiff > node.val - leftMax:
                    minDiff = node.val - leftMax

            rightMin = math.maxint
            if node.right:
                rightMin, maxV = getMinMax(node.right)

                if minDiff > rightMin - node.val:
                    minDiff = node.val - leftMax

            return minV, maxV

        return minDiff