class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        rv = []
        def explore(currstring, index):
            if index >= len(digits):
                if currstring:
                    rv.append(currstring)
                return
            for letter in mapping[digits[index]]:
                explore(currstring + letter, index+1)
        
        explore('', 0)
        return rv

    