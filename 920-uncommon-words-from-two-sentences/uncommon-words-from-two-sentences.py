class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ls1 = s1.split(" ")
        ls2 = s2.split(" ")
        ls1.extend(ls2)
        di = defaultdict(int)
        for word in ls1:
            di[word] += 1
        return [word for word in di.keys() if di[word] == 1]