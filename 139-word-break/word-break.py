class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) +1)]
        dp[0] = True

        word_dict_set = set(wordDict)
        for i in range(len(dp)):
            for word in wordDict:
                n = len(word)
                if i-n >= 0 and dp[i-n] and s[i-n:i] == word:
                    dp[i] = True
                    break

        print(dp)
        return dp[-1]

