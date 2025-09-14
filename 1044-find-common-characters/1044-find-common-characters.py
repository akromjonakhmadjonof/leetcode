from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = {}

        for word in words:
            for char, count in Counter(word).items():
                if char not in freq:
                    freq[char] = [count]
                else:
                    freq[char].append(count)
        results = []

        for char, counts in freq.items():
            if len(counts) == len(words):
                results.extend([char] * min(counts))
        return results