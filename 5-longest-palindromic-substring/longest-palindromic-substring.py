class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        
        def explore(i, j):
            l = i
            r = j
            curr = ''
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
                curr = s[l+1:r]
            return curr
        allperms = [max(explore(k, k), explore(k, k+1), key=len) for k in range(len(s) -1)]
        return max(allperms, key = len)