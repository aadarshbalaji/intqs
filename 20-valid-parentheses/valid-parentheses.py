class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        op = ['(', '[', '{']
        cl = [')', ']', '}']
        for character in s:
            if character in op:
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                check = stack.pop()
                if check == op[cl.index(character)]:
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True