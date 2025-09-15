class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters) # Turn into set for O(1) search
        count = 0 # Counts the number of words that can be fully typed
        for word in text.split(" "):
            if all(char not in brokenLetters for char in list(set(word))):
                count += 1
        return count