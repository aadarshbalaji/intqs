class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rv = []
        def helper(o, c, curr):
            if o == c == n:
                rv.append(str(curr))
                return
            if c < o <= n:
                helper(o, c+1, curr+')')
            if o < n:
                helper(o+1, c, curr+'(')
        helper(0,0,'')
        return rv