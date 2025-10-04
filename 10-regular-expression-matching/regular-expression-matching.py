class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        #key will be (i, j) true/false

        memo = {}

        def match(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            
            if j == m:
                memo[(i,j)] = (i == n)
                return memo[(i,j)]
            
            first_match = (i < n) and (p[j] == s[i] or p[j] == '.')

            if (j + 1) < m and p[j+1] == '*':
                skip_star = match(i, j + 2)

                use_star = first_match and match(i + 1, j)
                memo[(i,j)] = (skip_star or use_star)

                return memo[(i,j)]
            
            if first_match:
                memo[(i,j)]= match(i + 1, j + 1)
                return memo[(i,j)]
            else:
                memo[(i,j)] = False
                return False
        
        return match(0,0)
 