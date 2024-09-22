class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        left = 0
        seen = {}
        for r, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            maxlen = max(maxlen, r - left + 1)
            seen[c] = r
        return maxlen

