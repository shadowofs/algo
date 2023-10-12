from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        size = len(prices)
        dp = [0 for _ in range(size)]

        v = prices[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1], prices[i] - v)

            if prices[i] < v:
                v = prices[i]

        v = prices[-1]
        for i in range(size - 2, -1, -1):
            if prices[i] < v:
                dp[i] += v - prices[i]
            else:
                v = prices[i]

        return max(dp)


if __name__ == "__main__":
    print(Solution().maxProfit([3,3,5,0,0,3,1,4]))