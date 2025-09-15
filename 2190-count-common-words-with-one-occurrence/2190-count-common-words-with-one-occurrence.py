from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = Counter(words1) # Stores frequency of words in words1
        words2 = Counter(words2) # Stores frequency of words in words2
        counter = 0 # Counts how many common words with one occurance
        for word, count in words1.items():
            if count == 1 and word in words2 and words2[word] == 1:
                counter += 1
        return counter