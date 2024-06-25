class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = []
        rvlist = []
        for word in strs:
            h = {letter:word.count(letter) for letter in word}
            if h in maps:
                rvlist[maps.index(h)].append(word)
            else:
                maps.append(h)
                rvlist.append([word])
        return rvlist


