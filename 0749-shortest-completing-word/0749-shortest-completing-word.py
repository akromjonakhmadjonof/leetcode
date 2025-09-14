from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        frequency = {} # Stores frequencies of required letters
        for char in licensePlate:
            if char.isalpha():
              char = char.lower()
              frequency[char] =  frequency.get(char, 0) + 1
        
        completing_word = None # Stores shortest completing word
        for word in words:
            word_count = Counter(word.lower()) # Stores frequenct of chars in the word
            valid = True # 

            for char, count in frequency.items():
                if word_count[char] < count:
                    valid = False
                    break
            # If word is valid and shorter then current result, result will be updated
            if valid and (not completing_word or len(word) < len(completing_word)):
                completing_word = word
        
        
        return completing_word