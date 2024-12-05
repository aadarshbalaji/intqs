class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        all_letters = list('abcdefghijklmnopqrstuvwxyz')
        q = deque()
        new = set(wordList)
        count = 0
        q.append(beginWord)

        def connected(word):
            rv = []
            for i in range(len(word)):
                for letter in all_letters:
                    rv.append(word[0:i] + letter + word[i+1:])
            return rv
        while q:
            size = len(q)
            count += 1
            for i in range(size):
                currword = q.popleft()
                if currword == endWord:
                    return count
                for neighbor in connected(currword):
                    if neighbor in new:
                        new.remove(neighbor)
                        q.append(neighbor)
        return 0