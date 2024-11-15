class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        curr = ''
        def expand(i, j):
            l = i
            r = j
            curr = ''
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = max(curr, s[l:r+1], key=len)
                l -= 1
                r += 1
            return curr
        
        return max([max(expand(k,k),expand(k, k+1), key=len) for k in range(len(s))], key=len)
                


