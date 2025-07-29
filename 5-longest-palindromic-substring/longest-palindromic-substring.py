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
            return s[i+1:j]

        
        rvlist = [max(explore(x,x+1), explore(x,x), key=len) for x in range(len(s))]
        return max(rvlist, key=len)