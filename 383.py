class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        bm = [0] * 26
        for i in range(len(magazine)):
            bm[ord(magazine[i]) - ord('a')] += 1

        for i in range(len(ransomNote)):
            bm[ord(ransomNote[i]) - ord('a')] -= 1
            if bm[ord(ransomNote[i]) - ord('a')] < 0:
                return False

        return True


if __name__ == '__main__':
    print(Solution().canConstruct("aa","aab"))