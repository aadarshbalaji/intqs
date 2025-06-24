class Trie:

    def __init__(self):
        self.root = {}


    def insert(self, word: str) -> None:
        curr = self.root
        for i, letter in enumerate(word):
            if i == len(word) - 1:
                if letter in curr:
                    curr[letter]['*'] = True
                else:
                    curr[letter] = {}
                    curr[letter]['*'] = True
            elif letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
    def search(self, word: str) -> bool:
        curr = self.root
        for i, letter in enumerate(word):
            if i == len(word) - 1:
                if letter in curr and '*' in curr[letter]:
                    return True
                else:
                    return False
            if letter not in curr:
                return False
            else:
                curr = curr[letter]

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, letter in enumerate(prefix):
            if i == len(prefix) - 1:
                if letter in curr:
                    return True
                else:
                    return False
            if letter not in curr:
                return False
            else:
                curr = curr[letter]
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)