class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        currdict = defaultdict(int)
        if len(s) < n:
            return []
        rv = []
        check = Counter(p)
        i= 0
        while i < n:
            currdict[s[i]] += 1
            i += 1
        

        while i < len(s):
            if currdict == check:
                rv.append(i-n)
            currdict[s[i-n]] -= 1
            if currdict[s[i-n]] == 0:
                del currdict[s[i-n]]
            currdict[s[i]] += 1
            i += 1
        if currdict == check:
            rv.append(i-n)
        return rv

        