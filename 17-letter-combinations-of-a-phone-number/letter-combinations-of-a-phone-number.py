class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combos = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        rv = []
        def helper(index, curr):
            if index >= len(digits):
                rv.append(str(curr))
                return
            for c in combos[int(digits[index])]:
                curr += c
                helper(index+1, curr)
                curr = curr[:-1]

        helper(0, '')
        return rv