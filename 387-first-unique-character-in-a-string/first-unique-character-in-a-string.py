class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        abc = [0] * 26
        for c in s:
            abc[ord(c)-ord('a')] += 1
        #print(abc)
        for i,c in enumerate(s):
            if abc[ord(c) - ord('a')] == 1:
                return i
        return -1