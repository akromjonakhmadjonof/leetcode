class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        results = []

        for i in range(len(words)):
            if x in set(words[i]):
                results.append(i)
        return results
