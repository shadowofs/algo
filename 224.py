class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        digit = 0

        def consume(num) -> int:
            result = 0
            if len(stack) == 0:
                return num
            pre = stack.pop()
            while pre != '(':
                if pre == '-':
                    result += -num
                    num = 0
                elif pre == '+':
                    result += num
                    num = 0
                else:
                    num = pre

                if len(stack) == 0:
                    break
                pre = stack.pop()

            return result + num

        for c in s:
            if c == " ":
                continue
            if c in {"+", "-", "("}:
                if digit != 0:
                    stack.append(digit)
                    digit = 0
                stack.append(c)
            elif c == ")":
                stack.append(consume(digit))
                digit = 0
            else:
                digit = digit * 10 + int(c)

        return consume(digit)


if __name__ == "__main__":
    print(Solution().calculate("-1"))
