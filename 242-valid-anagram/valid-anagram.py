class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] += 1
        for x in t:
            count[ord(x)-ord('a')] -= 1
        for y in count:
            if y != 0:
                return False
        return True
        
