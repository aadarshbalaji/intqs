class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        r = 0
        maxlen = 0
        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            maxlen = max(maxlen, r-l+1)
            seen[c] = r
        return maxlen