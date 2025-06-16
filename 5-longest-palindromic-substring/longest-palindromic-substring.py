class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def explore(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1: j]
        
        return max([max(explore(i,i), explore(i,i+1), key=len) for i in range(len(s))], key=len)