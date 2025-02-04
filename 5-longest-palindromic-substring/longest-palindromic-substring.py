class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        def explore(i, j):
            currmax = ''
            l = i
            r = j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                currmax = max(currmax, s[l+1: r], key=len)
            return currmax
        
        allexplorations = [max(explore(k,k+1), explore(k,k), key=len) for k in range(len(s)-1)]
        if len(allexplorations) > 0:
            return max(allexplorations, key=len)
        else:
            return ""