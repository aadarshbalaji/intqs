class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currstring = ''
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
                currstring = string + currstring * num
            else:
                currstring += c
        
        while stack:
            currstring = stack.pop() + currstring
        
        return currstring