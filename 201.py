class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        base = 1
        res = 0
        while base <= right:
            s = left - left % base
            while s <= right:
                if s & base == 0:
                    break
                s += base
            else:
                res += base

            base <<= 1

        return res


if __name__ == "__main__":
    print(Solution().rangeBitwiseAnd(3,4))