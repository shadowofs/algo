class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp = [[False for i in range(size)] for j in range(size)]

        def palindrome(i: int, j: int) -> bool:
            if i >= j:
                return True

            return dp[i][j]

        maxl = 1
        maxi = 0
        for offset in range(2, size+1):
            for start in range(0, size):
                end = start+offset-1
                if end >= size:
                    break

                dp[start][end] = palindrome(start + 1, end - 1) and s[start] == s[end]

                if dp[start][end] and offset > maxl:
                    maxl = offset
                    maxi = start

        return s[maxi:maxi + maxl]


if __name__ == "__main__":
    print(Solution().longestPalindrome("aaaaa"))