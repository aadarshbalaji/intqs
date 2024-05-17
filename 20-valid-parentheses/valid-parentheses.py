class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        for let in s:
            if let not in d:
                stack.append(let)
                continue
            if not stack or stack[-1] != d[let]:
                return False
            stack.pop()

        return not stack