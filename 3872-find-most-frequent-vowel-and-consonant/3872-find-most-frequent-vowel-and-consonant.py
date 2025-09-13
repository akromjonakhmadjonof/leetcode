from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {"a", "e", "i", "o", "u"} # Vowels
        counter = Counter(s) # Frequincies of chars in the given string
        max_vowel = 0 # Stores maximum frequicy of a vowel character
        max_other = 0 # Stores maximum frequicy of an other non-vowel character 

        for char, count in counter.items():
            if char in vowels:
                max_vowel = max(max_vowel, count) 
            else:
                max_other = max(max_other, count)
        return max_vowel + max_other 