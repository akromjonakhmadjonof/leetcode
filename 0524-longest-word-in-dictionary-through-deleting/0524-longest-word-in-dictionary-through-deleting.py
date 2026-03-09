class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""
        for word in dictionary:
            i = j = 0
            while j < len(word) and i < len(s):
                if word[j] == s[i]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word):
                if len(result) == 0:
                    result = word
                elif len(word) > len(result):
                    result = word
                elif len(word) == len(result):
                    result = min(word, result)
        return result