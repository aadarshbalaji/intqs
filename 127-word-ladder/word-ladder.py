class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        new = set(wordList)
        q = deque([beginWord])
        count = 0
        letters = list('abcdefghijklmnopqrstuvwxyz')
        def connected(word):
            rv = []
            for i in range(len(word)):
                for letter in letters:
                    rv.append(word[0:i] + letter + word[i+1:])
            return rv
        while q:
            count += 1
            size = len(q)
            for i in range(size):
                currword = q.popleft()
                if currword == endWord:
                    return count
                for neighbor in connected(currword):
                    if neighbor in new:
                        new.remove(neighbor)
                        q.append(neighbor)
        return 0