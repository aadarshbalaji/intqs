class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        curr = ''
        def expand(l, r):
            count = 0
            cs = ''
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count = r-l+1
                cs = s[l:r+1]
                l -=1
                r += 1
            return cs
        
        for i in range(len(s)):
            curr = max(curr, expand(i, i), expand(i, i+1), key=len)
        return curr

