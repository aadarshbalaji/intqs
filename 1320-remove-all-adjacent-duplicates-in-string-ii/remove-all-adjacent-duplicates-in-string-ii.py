class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['', 0]]
        for c in s:
            if stack[-1][0] == c:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([c,1])
        ans = ""
        while stack:
            s, n = stack.pop()
            ans = s * n + ans
        return ans
