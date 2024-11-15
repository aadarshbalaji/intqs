class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        n = len(s)
        def explore(index, curr):
            if index >= n:
                res.append(list(curr))
            for i in range(index, n):
                sub = s[index: i + 1]
                if sub == sub[::-1]:
                    curr.append(sub)
                    explore(i + 1, curr)
                    curr.pop()
        explore(0, [])
        return res
