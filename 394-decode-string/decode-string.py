class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currnum = 0
        currstring = ''
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
                currstring = string + currstring*num
            else:
                currstring += c
        
        return currstring

        