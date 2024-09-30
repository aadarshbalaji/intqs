class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(o, c, string):
            if o == c == n:
                ans.append(string)
                return

            if o < n:
                dfs(o+1,c,string+'(')

            if c < o:
                dfs(o, c + 1, string+')')


        dfs(0, 0, "")
        
        return ans