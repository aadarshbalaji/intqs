class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        currmax = 0
        seen = {}
        for r, letter in enumerate(s):
            if letter in seen and seen[letter] >= l:
                l = seen[letter] + 1
            currmax = max(currmax, r-l+1)
            seen[letter] = r
        return currmax