class Solution:
    def reverseBits(self, n: int) -> int:
        base = 1
        rev = 1 << 31
        res = 0
        for i in range(32):
            if rev & n > 0:
                res += base

            base <<= 1
            rev >>= 1

        return res


