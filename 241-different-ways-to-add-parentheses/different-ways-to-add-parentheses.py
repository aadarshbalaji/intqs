class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):
            curr = expression[i]
            if curr == '+' or curr == '-' or curr == '*':
                left = expression[0:i]
                right = expression[i+1:]
                s1 = self.diffWaysToCompute(left)
                s2 = self.diffWaysToCompute(right)

                for i in s1:
                    for j in s2:
                        if curr == '+':
                            res.append(int(i) + int(j))
                        if curr == "*":
                            res.append(int(i) * int(j))
                        if curr == '-':
                            res.append(int(i) - int(j))
        if len(res) == 0:
            res.append(int(expression))
        return res

