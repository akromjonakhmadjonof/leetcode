from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        seen = set()
        count = 0
        for char in word:
            if char.lower() not in seen:
                if (char.islower() and char.upper() in word) or (char.isupper() and char.lower() in word):
                    count += 1
                    seen.add(char.lower())
        return count

