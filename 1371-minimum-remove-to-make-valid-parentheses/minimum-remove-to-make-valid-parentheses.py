class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        indices = set()
        for i,c in enumerate(s):
            if c == '(':
                stack.append([i, c])
            if c == ')':
                if not stack or stack[-1][1] != '(':
                    indices.add(i)
                else:
                    stack.pop()
        while stack:
            indices.add(stack.pop()[0])
        
        newstr = ''
        for i in range(len(s)):
            if i not in indices:
                newstr += s[i]
        return newstr
        
