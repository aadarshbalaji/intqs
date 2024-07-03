class Solution:
    def addBinary(self, a: str, b: str) -> str:
        vala = 0
        return str(bin(int(a,2)+int(b,2)))[2:]
        for index, value in enumerate(reversed(a)):
            if value == 1:
                vala += 2 ** index
            else:
                continue
        valb = 0
        for index, value in enumerate(reversed(b)):
            if value == 1:
                valb += 2 ** index
            else:
                continue
        print(vala + valb)
        return str(bin(vala + valb))[2:]
