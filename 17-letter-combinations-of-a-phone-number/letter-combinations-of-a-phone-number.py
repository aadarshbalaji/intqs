class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {2: 'abc', 3: 'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        rv=[]
        def backtrack(index, path):
            if index == len(digits):
                rv.append(str(path))
                return
            choices = [s for s in mapping[int(digits[index])]]
            for c in choices:
                new = path + c
                backtrack(index + 1, new)
        
        backtrack(0, '')
        if not rv or (len(rv)==1 and rv[0] == ""):
            return []
        return rv
