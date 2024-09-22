class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0] * 26
        for x in s:
            chars[ord(x) - ord('a')] += 1
        for x in t:
            chars[ord(x) - ord('a')] -= 1
        for num in chars:
            if num != 0:
                return False
        return True