class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        find middle index, go outwards
        """
        def expand(i, j):
            state = s[i:j]
            while i >= 0 and j < len(s) and s[i] == s[j]:
                state = s[i:j+1]
                i -= 1
                j += 1
            return state
        currmax = ""
        for i in range(len(s)):
            currmax = max(currmax, expand(i,i), expand(i,i+1), key=len)
        return currmax

