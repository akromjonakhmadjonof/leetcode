class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters) # Turn into set for O(1) search
        count = 0 # Counts the number of words that can't be fully typed
        for word in text.split(" "):
            for char in word:
                if char in brokenLetters:
                    count += 1
                    break
            
        return len(text.split(" ")) - count