# encoding: utf-8
# a = input("please input a number:")
def repeat(s):
    length = len(s)
    subLen = 1
    while subLen <= length // 2:
        if length % subLen != 0:
            subLen += 1
            continue

        cur = 0
        while cur < length:
            if s[cur % subLen] != s[cur]:
                break
            cur += 1
        if cur == length:
            return True

        subLen += 1

    return False


if __name__ == "__main__":
    print(repeat("abab"))
    print(repeat("aba"))
    print(repeat("abcabcabc"))
