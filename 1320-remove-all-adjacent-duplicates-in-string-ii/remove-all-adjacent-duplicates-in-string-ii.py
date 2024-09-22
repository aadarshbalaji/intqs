class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop(-1)
            else:
                stack.append([c,1])
        
        ans = ''
        for s,c in stack:
            ans += s*c
        return ans