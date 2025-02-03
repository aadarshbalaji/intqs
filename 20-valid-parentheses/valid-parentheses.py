class Solution:
    def isValid(self, s: str) -> bool:
        hs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c not in hs:
                stack.append(c)
            elif not stack or hs[c] != stack.pop():
                return False
        return len(stack) == 0
            