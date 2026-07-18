from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        same letters, same freq
        """
        freq_s = Counter(s)
        freq_t = Counter(t)
        return freq_s == freq_t
        