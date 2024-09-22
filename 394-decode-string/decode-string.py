class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currstring = ''
        currnum = 0
        for c in s:
            if c.isdigit():
                currnum = currnum*10 + int(c)
            elif c == '[':
                stack.append(currnum)
                stack.append(currstring)
                currstring = ''
                currnum = 0

            elif c == ']':
                s = stack.pop()
                num = stack.pop()
                currstring = s + currstring*num
                
            else:
                currstring += c
        while stack:
            currstring = currstring + stack.pop()
        return currstring

                

        