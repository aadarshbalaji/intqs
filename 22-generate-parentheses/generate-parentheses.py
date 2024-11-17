class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(o, c, curr):
            if o == c == n:
                ans.append(str(curr))
                return
            if o < n:
                curr += '('
                backtrack(o+1, c, curr)
                curr = curr[:-1]
            if c < o:
                curr += ')'
                backtrack(o, c+1, curr)
                curr = curr[:-1]
        backtrack(0,0,'')
        return ans


