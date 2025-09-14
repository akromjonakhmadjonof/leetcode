from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = {} # Stores frequency of words in each s1 and s2
        results = [] # Stores the results, unique words in each strings
        # Maps each word in s1 and s2 to freq
        for word in s1.split():
            freq[word] = freq.get(word, 0) + 1
        for word in s2.split():
            freq[word] = freq.get(word, 0) + 1
        # Find words with frequency of 1
        for word, count in freq.items():
            if count == 1:
                results.append(word)
        return results