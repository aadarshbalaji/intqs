class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_sub = 0
        for i, letter in enumerate(s):
            if letter in seen and seen[letter] >= start:
                start = seen[letter] + 1
            max_sub = max(max_sub, i-start+1)
            seen[letter] = i

        return max_sub

