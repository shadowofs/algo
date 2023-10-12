class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len + s2_len != len(s3):
            return False

        dp = [[False for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]
        dp[0][0] = True
        for i in range(s1_len+1):
            for j in range(s2_len+1):
                offset = i + j - 1
                if offset < 0:
                    continue

                if j > 0:
                    if dp[i][j-1] and s3[offset] == s2[j-1]:
                        dp[i][j] = True
                        continue

                if i > 0:
                    if dp[i-1][j] and s3[offset] == s1[i-1]:
                        dp[i][j] = True
                        continue

        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().isInterleave("", "", "a"))