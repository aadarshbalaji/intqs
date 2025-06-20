class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        before = self.countAndSay(n-1)
        print(before)
        curr = ""
        i = 0
        while i < len(before):
            count = 0
            currletter = before[i]
            while i < len(before) and currletter == before[i]:
                count += 1
                i += 1
            if count > 0:
                curr += str(count) + currletter 

        return curr
                
