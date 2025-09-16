from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars) # Stores frequency of chars

        words = [Counter(word) for word in words] # Turns into array of strings to array of frequency of strings
        
        def helper(word):
            length = 0
            # Check if we can make the given string from the given chars
            for char, count in word.items():
                length += count
                # If even one element is more then given chars then we have to return 0 otherwise return length of string
                if not chars[char] >= count:
                    return 0
            return length
                
        total = 0
        for word in words:
            total += helper(word)
        return total
            