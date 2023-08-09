class Solution:
    def isHappy(self, n: int) -> bool:
        known = {n}
        nn = self.ssum(n)
        while nn != 1 and nn not in known:
            known.add(nn)
            nn = self.ssum(nn)

        return nn == 1

    def ssum(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += (n % 10) ** 2
            n = int(n / 10)

        return ans


if __name__ == '__main__':
    print(Solution().isHappy(7))