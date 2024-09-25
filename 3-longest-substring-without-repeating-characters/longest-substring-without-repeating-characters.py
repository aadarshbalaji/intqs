class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        currmax = 0
        if len(s) == len(set(s)):
            return len(s)
        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            currmax = max(currmax, r-l+1)
            seen[s[r]] = r
        return currmax
