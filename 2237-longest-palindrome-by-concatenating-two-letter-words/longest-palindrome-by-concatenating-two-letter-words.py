class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        counter = Counter(words)
        ans = 0
        has_center = False
        for word, count in counter.items():
            if word[0] == word[1]:
                if count % 2 == 1:
                    has_center = True
                ans += (count // 2) * 4
            elif word < word[::-1]:
                ans += min(count, counter[word[::-1]]) * 4
        ans = ans + (2 if has_center else 0)
        return ans



