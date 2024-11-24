class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        rv = []
        n = len(s)
        def explore(index, path):
            if index == n:
                rv.append(list(path))
            for i in range(index, n):
                sub = s[index:i+1]
                if sub == sub[::-1]:
                    path.append(sub)
                    explore(i+1, path)
                    path.pop()
        explore(0, [])
        return rv