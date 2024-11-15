class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        def expand(i, j):
            l = i
            r = j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        return max([max(expand(k,k),expand(k, k+1), key=len) for k in range(len(s))], key=len)
                


