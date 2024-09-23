class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currstring = ""
        currnum = 0
        for c in s:
            if c.isdigit():
                currnum = currnum * 10 + int(c)

            elif c == '[':
                stack.append(currnum)
                stack.append(currstring)
                currnum = 0
                currstring = ''
            elif c == ']':
                string = stack.pop()
                num = stack.pop()
                currstring = string + num * currstring

            else:
                currstring += c
        while stack:
            currstring = stack.pop() + currstring
        return currstring