class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in matching.keys(): #opening
                stack.append(c)
            else:
                if not stack or matching[c] != stack.pop():
                    return False
        return True if len(stack) == 0 else False
        