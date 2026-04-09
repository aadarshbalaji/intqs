class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        r = 0
        max_sub = 0
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            max_sub = max(max_sub, r-l+1)
            seen[s[r]] = r
            r += 1

        return max_sub

