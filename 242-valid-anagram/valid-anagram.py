class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26
        for c in s:
            chars[ord(c) - ord('a')] += 1 
        for x in t:
            chars[ord(x) - ord('a')] -= 1 
        
        for c in chars:
            if c != 0:
                return False
        return True