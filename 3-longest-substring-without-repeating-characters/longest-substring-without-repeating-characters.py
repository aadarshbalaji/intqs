class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        maxlen = 0
        for r, letter in enumerate(s):
            if letter in seen and seen[letter] >= l:
                l = seen[letter] + 1
            maxlen = max(maxlen, r-l+1)
            seen[letter] = r
        return maxlen
