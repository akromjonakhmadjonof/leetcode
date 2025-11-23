class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        results = []

        for index, word in enumerate(words):
            if x in set(word):
                results.append(index)
        return results
