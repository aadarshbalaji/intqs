class Solution:
    def isValid(self, s: str) -> bool:
        hs = {'}':'{', ')': '(', ']':'['}
        stack = []
        for c in s:
            if c in hs:
                if not stack or hs[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return len(stack) == 0