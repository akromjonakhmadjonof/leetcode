class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev = ""
        for word in words:
            anagram = "".join(sorted(word))
            if anagram != prev:
                result.append(word)
                prev = anagram
        return result
