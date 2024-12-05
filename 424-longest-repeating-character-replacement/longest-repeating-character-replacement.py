class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        frequency_map = defaultdict(int)
        max_freq = 0
        longest_substring_length = 0
        for end in range(len(s)):
            frequency_map[s[end]] += 1
            max_freq = max(max_freq, frequency_map[s[end]])
            if end - start + 1  - max_freq > k:
                frequency_map[s[start]] -= 1
                start += 1
            longest_substring_length = max(longest_substring_length, end-start+1)
        return longest_substring_length
                