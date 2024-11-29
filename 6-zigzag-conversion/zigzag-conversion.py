class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        down = True
        arr = [[] for i in range(numRows)]

        i = 0
        row = 0
        while i < len(s):
            if down:
                for j in range(numRows):
                    if i < len(s):
                        arr[j].append(s[i])
                        i += 1
                down = not down
            else:
                for j in range(numRows-2,0,-1):
                    if i < len(s):
                        arr[j].append(s[i])
                        i += 1
                down = not down
        rv = ''
        for a in arr:
            rv += ''.join(a)
        return rv