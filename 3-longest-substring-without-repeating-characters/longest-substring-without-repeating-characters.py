class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        currmax = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen:
                if seen[s[r]] >= l:
                    l = seen[s[r]] + 1
            currmax = max(currmax, r-l+1)
            seen[s[r]] = r
        return currmax