class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rv = []
        curr = ''
        for c in s:
            if c == ' ':
                rv.append(curr)
                curr = ''
            else:
                curr = curr + c
        rv.append(curr)
        rv = [x for x in rv if len(x)>0]
        return ' '.join(reversed(rv))
        