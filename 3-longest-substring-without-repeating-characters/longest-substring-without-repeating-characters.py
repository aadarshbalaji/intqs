class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxlen = 0
        l = 0
        for r, c in enumerate(s):
            if c in seen:
                if seen[c] >= l:
                    l = seen[c] + 1
            maxlen = max(maxlen, r-l+1)
            seen[c] = r
        return maxlen
