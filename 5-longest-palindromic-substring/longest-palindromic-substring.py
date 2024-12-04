class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        def explore(i, j):
            currstring = ''
            while i >= 0 and j < len(s) and s[i] == s[j]:
                currstring = max(currstring, s[i:j+1], key=len)
                i -= 1
                j += 1
            return currstring
        
        print(explore(2,2))
        currmax = ''
        for i in range(len(s)):
            currmax = max(currmax, explore(i,i), explore(i,i+1), key=len)
        return currmax



