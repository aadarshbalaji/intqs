class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0
        for character in s:
            if character.isdigit():
                num = num * 10 + int(character)
            elif character == '[':
                stack.append(num)
                stack.append(curr)
                num = 0 
                curr = ""
            elif character == ']':
                prevstring = stack.pop()
                prevnum = stack.pop()
                curr = prevstring + curr * prevnum
            else:
                curr += character
        while stack:
            curr = stack.pop() + curr
        return curr

