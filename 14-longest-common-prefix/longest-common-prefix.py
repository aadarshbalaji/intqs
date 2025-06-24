class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        curr = ""
        while pointer < len(strs[0]):
            match = strs[0][pointer]
            for word in strs[1:]:
                if pointer >= len(word) or word[pointer] != match:
                    return curr
            curr += match
            pointer += 1
        return curr
