class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = 0, 0
        n1, n2 = len(word1), len(word2)
        merged = ""
        while first < n1 and second < n2:
            merged += word1[first] + word2[second]
            first += 1
            second += 1
        if first < n1:
            merged += word1[first:]
        if second < n2:
            merged += word2[second:]
        return merged