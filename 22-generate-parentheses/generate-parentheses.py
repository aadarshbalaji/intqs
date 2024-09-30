class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(o, c, curr):
            if o == c == n:
                ans.append(curr)
                return
            if o < n:
                dfs(o+1, c, curr+'(')
            if c < o:
                dfs(o, c+1, curr+')')

        dfs(0,0,"")
        return ans